#
#  Copyright 2019 The FATE Authors. All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
from peewee import Model
import datetime
from arch.api.utils import log_utils
from peewee import CharField, IntegerField, BigIntegerField, DateTimeField

LOGGER = log_utils.getLogger()

class DataBaseModel(Model):
    class Meta:
        database = DB

    def to_json(self):
        return self.__dict__['__data__']

    def save(self, *args, **kwargs):
        if hasattr(self, "update_date"):
            self.update_date = datetime.datetime.now()
        super(DataBaseModel, self).save(*args, **kwargs)


class MachineLearningModelInfo(DataBaseModel):
    id = BigIntegerField(primary_key=True)
    sceneId = IntegerField(index=True)
    myPartyId = IntegerField(index=True)
    partnerPartyId = IntegerField(index=True)
    myRole = CharField(max_length=10, index=True)
    commitId = CharField(max_length=50, index=True)
    commitLog = CharField(max_length=500, default='')
    jobId = CharField(max_length=50, index=True)
    tag = CharField(max_length=50, default='', index=True)
    createDate = DateTimeField(index=True)
    updateDate = DateTimeField(index=True)

    class Meta:
        db_table = "machine_learning_model_info"
    # DTable
    # scene_key: sceneId_myPartyId_partnerPartyId_myRole
    # version info, nameSpace: mlmodel_version, name: scene_key, k: commitId, v: {commitLog:xx, timestamp: xx, parentId: xx, tableName: xx, tabkeNameSpace: xx}
    # model data, nameSpace: scene_key_"model_data", name:  commitId, k: model_meta/model_param/data_transform, v: bytes


class FeatureDataInfo(DataBaseModel):
    id = BigIntegerField(primary_key=True)
    sceneId = IntegerField(index=True)
    myPartyId = IntegerField(index=True)
    partnerPartyId = IntegerField(index=True)
    myRole = CharField(max_length=10, index=True)
    commitId = CharField(max_length=50, index=True)
    commitLog = CharField(max_length=500, default='')
    dataType = CharField(max_length=200, index=True)
    jobId = CharField(max_length=50, index=True)
    tag = CharField(max_length=50, default='', index=True)
    createDate = DateTimeField(index=True)
    updateDate = DateTimeField(index=True)

    class Meta:
        db_table = "feature_data_info"
    # DTable
    # scene_key: sceneId_myPartyId_partnerPartyId_myRole
    # version info, nameSpace: feature_data_version, name: scene_key, k: commitId, v: {commitLog:xx, timestamp: xx, parentId: xx, tableName: xx, tabkeNameSpace: xx}
    # feature data, nameSpace: scene_key_"feature_data", name:  commitId, k: sid, v: string
    # feature meta, nameSpace: scene_key_"feature_meta", name:  commitId, k: feature_name, v: feature_index
    # feature header, nameSpace: scene_key_"feature_header", name:  commitId, k: features/labels, v: object
