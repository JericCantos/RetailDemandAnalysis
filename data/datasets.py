

file_urls = {
    # Original Tables
    "holiday_events": "https://drive.google.com/uc?id=1RMjSuqHXHTwAw_PGD5XVjhA3agaAGHDH",
    "items": "https://drive.google.com/uc?id=1ogMRixVhNY6XOJtIRtkRllyOyzw1nqya",
    "oil": "https://drive.google.com/uc?id=1Q59vk2v4WQ-Rpc9t2nqHcsZM3QWGFje_",
    "stores": "https://drive.google.com/uc?id=1Ei0MUXmNhmOcmrlPad8oklnFEDM95cDi",
    "train": "https://drive.google.com/uc?id=1oEX8NEJPY7wPmSJ0n7lO1JUFYyZjFBRv",
    "transactions": "https://drive.google.com/uc?id=1PW5LnAEAiL43fI5CRDn_h6pgDG5rtBW_",

    # Pickled transactions
    "preliminary": "https://drive.google.com/file/d/1-slDnCsV-V-v1aS7maViZPiHIbLDWOv3",
        # contains rows of "train" belonging to the Guayas region, and only relating
        # to products from the top 3 families (GROCERY I,  BEVERAGES, and CLEANING)
    "cleaned": "https://drive.google.com/file/d/1otcA0OoYn1QnG-hU-zKA-QfFsJ7g4HUX",
        # preliminary dataset with days with 0 sales filled in, outliers tagged and 
        # winsorized, boolean flags set (including holiday marker), merged with df_items
        # and df_stores to include some item- and store-level information, and with 
        # date components extracted.
    "engineered": "https://drive.google.com/file/d/164KmgUNQwex1qQUc7W9WTdThcY65nHc-"
        # from the cleaned dataset, filtered only for records dated Jan 1 - Mar 31, 2014.
        # introduced lags and rolling statistics to feed to the prediction model
}