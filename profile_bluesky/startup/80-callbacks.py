print(__file__)

# custom callbacks
from APS_BlueSky_tools.callbacks import DocumentCollectorCallback


doc_collector = DocumentCollectorCallback()
RE.subscribe(doc_collector.receiver)
