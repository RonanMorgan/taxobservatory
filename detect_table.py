from transformers import TableTransformerModel, TableTransformerConfig

# Initializing a Table Transformer microsoft/table-transformer-detection style configuration
configuration = TableTransformerConfig()

# Initializing a model from the microsoft/table-transformer-detection style configuration
model = TableTransformerModel(configuration)

# Accessing the model configuration
configuration = model.config