from gazette.spiders.base import FecamGazetteSpider


class ScAscurraSpider(FecamGazetteSpider):
    name = "sc_ascurra"
    FECAM_QUERY = 'cod_entidade:26'
    TERRITORY_ID = "4201703"