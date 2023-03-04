from pages.upload_file_page import UploadFilePage


class TestUploadFile:

    def test_upload_file(self, authorization, driver):
        upload_file_page = UploadFilePage(driver)
        file_name, file_extension = upload_file_page.upload_file()
        parse_name, parse_extension = upload_file_page.parse_files_from_table()
        assert (file_name, file_extension) == (parse_name, parse_extension)



