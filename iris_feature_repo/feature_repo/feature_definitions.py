from feast import Entity, FeatureView, Field, ValueType
from feast.types import Float32
from feast.infra.offline_stores.file_source import FileSource
from datetime import timedelta

# ------------------------
# Define Entity
# ------------------------
iris = Entity(
    name="iris_id",
    join_keys=["iris_id"],
    value_type=ValueType.INT64, 
)

# ------------------------
# Define Data Source
# ------------------------
iris_source = FileSource(
    path="data/iris.parquet",
    timestamp_field="event_timestamp",
)

# ------------------------
# Define Feature View
# ------------------------
iris_features = FeatureView(
    name="iris_features",
    entities=[iris],   # must pass Entity object
    ttl=timedelta(days=1),
    schema=[
        Field(name="sepal_length", dtype=Float32),
        Field(name="sepal_width", dtype=Float32),
        Field(name="petal_length", dtype=Float32),
        Field(name="petal_width", dtype=Float32),
    ],
    online=True,
    source=iris_source,
)