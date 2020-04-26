__version__ = '2.10.0'

import logging
from . import models, exceptions, defaults
from .api import Service, Bucket
from .auth import Auth, AuthV2, AnonymousAuth, StsAuth, AUTH_VERSION_1, AUTH_VERSION_2, make_auth
from .compat import to_bytes, to_string
from .crypto import LocalRsaProvider, RsaProvider, AliKMSProvider, EncryptionMaterials
from .crypto_bucket import CryptoBucket
from .iterators import (BucketIterator, ObjectIterator, MultipartUploadIterator, ObjectUploadIterator, PartIterator,
                        LiveChannelIterator)
from .models import BUCKET_ACL_PRIVATE, BUCKET_ACL_PUBLIC_READ, BUCKET_ACL_PUBLIC_READ_WRITE, \
    SERVER_SIDE_ENCRYPTION_AES256, SERVER_SIDE_ENCRYPTION_KMS
from .models import BUCKET_STORAGE_CLASS_STANDARD, BUCKET_STORAGE_CLASS_IA, BUCKET_STORAGE_CLASS_ARCHIVE, \
    BUCKET_STORAGE_CLASS_COLD_ARCHIVE
from .models import BUCKET_VERSIONING_ENABLE, BUCKET_VERSIONING_SUSPEND
from .models import OBJECT_ACL_DEFAULT, OBJECT_ACL_PRIVATE, OBJECT_ACL_PUBLIC_READ, OBJECT_ACL_PUBLIC_READ_WRITE
from .resumable import make_upload_store, make_download_store
from .resumable import resumable_upload, resumable_download, ResumableStore, ResumableDownloadStore, determine_part_size
from .utils import SizedFileAdapter, make_progress_adapter
from .utils import content_type_by_name, is_valid_bucket_name
from .utils import http_date, http_to_unixtime, iso8601_to_unixtime, date_to_iso8601, iso8601_to_date
from .http import CaseInsensitiveDict, Session
from .models import BUCKET_DATA_REDUNDANCY_TYPE_LRS, BUCKET_DATA_REDUNDANCY_TYPE_ZRS

logger = logging.getLogger('oss2')


def set_file_logger(file_path, name="oss2", level=logging.INFO, format_string=None):
    global logger
    if not format_string:
        format_string = "%(asctime)s %(name)s [%(levelname)s] %(thread)d : %(message)s"
    logger = logging.getLogger(name)
    logger.setLevel(level)
    fh = logging.FileHandler(file_path)
    fh.setLevel(level)
    formatter = logging.Formatter(format_string)
    fh.setFormatter(formatter)
    logger.addHandler(fh)


def set_stream_logger(name='oss2', level=logging.DEBUG, format_string=None):
    global logger
    if not format_string:
        format_string = "%(asctime)s %(name)s [%(levelname)s] %(thread)d : %(message)s"
    logger = logging.getLogger(name)
    logger.setLevel(level)
    fh = logging.StreamHandler()
    fh.setLevel(level)
    formatter = logging.Formatter(format_string)
    fh.setFormatter(formatter)
    logger.addHandler(fh)
