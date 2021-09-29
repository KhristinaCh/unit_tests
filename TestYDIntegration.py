import YD_Integration as yd


class TestIntegration:
# scenario with folder '1' as only existing folder in YD

    @classmethod
    def setup_class(cls):
        print('Cls method setup')

    def setup(self):
        print('method setup')

    def test_create_unexisting_folder(self):
        uploader = yd.YaUploader(yd.yd_token)
        assert uploader.create_folder('2') == 201

    def test_create_existing_folder(self):
        uploader = yd.YaUploader(yd.yd_token)
        assert uploader.create_folder('1') == 409

    def test_check_existing_folder(self):
        uploader = yd.YaUploader(yd.yd_token)
        assert uploader.check_folder('1') == 'success'

    def test_check_unexisting_folder(self):
        uploader = yd.YaUploader(yd.yd_token)
        assert uploader.check_folder('3') == 'no such folder'

    def teardown(self):
        print('Method teardown')

    @classmethod
    def teardown_cls(cls):
        print('Cls method teardown')