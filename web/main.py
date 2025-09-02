import streamlit as st
import pandas as pd
import os

class MainApp():
    def __init__(self):
        st.set_page_config(page_title="CSV Bulanan Modifier", page_icon='⌨', layout="wide")
        st.title('📊 CSV Bulanan Modifier')
        st.sidebar.header('Menu')
        self.nav_menu = st.sidebar.selectbox('Pilih Menu',
                             ['Home','Nominal Changer','Accounts Splitter'])
    
    def home(self):
        st.markdown(
            """
            ### Selamat datang di CSV Bulanan Modifier!
            
            Aplikasi ringan ini menggabungkan dua fitur utama:
            
            1. **Nominal Changer** - Ganti massal nilai identik dalam file CSV dengan cepat dan mudah.
            2. **Accounts Splitter** - Pisahkan otomatis CSV akun berdasarkan bank (Bank BSI & Mandiri).
            
            Alat ini menawarkan alternatif yang lebih cepat dan fleksibel dibandingkan generator CSV bawaan KPPN.
            """
        )
        
    def upload_file_handler(self):
        uploaded_file = st.file_uploader('Upload File CSV', type='csv')

        if not uploaded_file:
            st.error('Perhatian: File Belum diupload!')
        else:
            st.success('File Berhasil diupload')
            return uploaded_file
        
    def file_process_handler(self, uploaded_file_name, function: str):
        df_csv = pd.read_csv(uploaded_file_name, sep='|')
        st.write('Data Dari CSV')
        st.dataframe(df_csv)
        st.divider()
        if function == 'nominal changer':
            st.subheader('Proses Data')
            first_value = st.text_input('Nilai Awal')
            change_value = st.text_input('Nilai Akhir')
            btn_process_data = st.button('Proses & Preview Data')
            if btn_process_data:
                if not first_value or not change_value:
                    st.error('Belum Memasukkan Nominal')
                        
                else:
                    df_csv.loc[df_csv['JUMLAH_UANG'] == int(first_value), 'JUMLAH_UANG'] = int(change_value)
                    df_csv['NO'] = range(1, len(df_csv) + 1)
                    st.dataframe(df_csv)
                    new_df_to_csv = pd.DataFrame.to_csv(df_csv, index=False, sep='|')
                    file_name, _ = os.path.splitext(uploaded_file_name.name)
                    st.download_button('Download File Baru', new_df_to_csv, f'{file_name}_MODIFIKASI.csv', mime='text/csv')#TODO: auto rename filename
        
        elif function == 'account splitter':
            
            btn_divide = st.button('Pisahkan Data')
            if btn_divide:
                # mandiri
                mandiri_df = df_csv[df_csv['NO_REKENING'].astype(str).str.len() > 10]
                mandiri_df['NO'] = range(1, len(mandiri_df) + 1)
                # bsi
                bsi_df = df_csv[df_csv['NO_REKENING'].astype(str).str.len() <= 10]
                bsi_df['NO'] = range(1, len(bsi_df) + 1)
                
                st.subheader('Data Mandiri')
                st.dataframe(mandiri_df)
               
                st.subheader('Data BSI')
                st.dataframe(bsi_df)
                
                mandiri_to_csv = pd.DataFrame.to_csv(mandiri_df, index=False, sep='|')
                bsi_to_csv = pd.DataFrame.to_csv(bsi_df, index=False, sep='|')
                file_name, _ = os.path.splitext(uploaded_file_name.name)
                st.download_button('Download Mandiri Data', mandiri_to_csv, f'{file_name}_MANDIRI.csv', mime='text/csv')
                st.download_button('Download BSI Data', bsi_to_csv, f'{file_name}_BSI.csv', mime='text/csv')
                
        else:
            pass
        
    def nominal_changer_handler(self):
        st.subheader('Nominal Changer')
        st.text('Nominal Changer adalah aplikasi untuk memperbarui nilai secara massal dalam file CSV di mana sejumlah nominal tertentu sama. Alat ini berguna untuk mengoreksi atau menyesuaikan nilai transaksi yang berulang secara efisien.')
        uploaded_file = self.upload_file_handler()
        if uploaded_file:
            self.file_process_handler(uploaded_file,'nominal changer')
            
    def account_splitter_handler(self):
        st.subheader('Account Splitter')
        st.text('Account Splitter adalah aplikasi yang dirancang untuk memisahkan berbagai akun bank dengan cepat dan efisien, khususnya mendukung Bank BSI dan Bank Mandiri.')
        uploaded_file = self.upload_file_handler()
        if uploaded_file:
            self.file_process_handler(uploaded_file, 'account splitter')
            
if __name__ == '__main__':
    apps = MainApp()
    match apps.nav_menu:
        case 'Home':
            apps.home()
        
        case 'Nominal Changer':
            apps.nominal_changer_handler()
        
        case 'Accounts Splitter':
            apps.account_splitter_handler()
    