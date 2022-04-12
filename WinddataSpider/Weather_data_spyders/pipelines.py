from scrapy.pipelines.files import FilesPipeline


class WinddataspiderPipeline(FilesPipeline):
    def file_path(self, request, response=None, info=None):
        return request.url.split('/')[-1]
