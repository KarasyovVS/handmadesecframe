class GetPathUtil:

    @staticmethod
    def get_path(url):
        url_list = url.split("/")
        return url_list[-1]
