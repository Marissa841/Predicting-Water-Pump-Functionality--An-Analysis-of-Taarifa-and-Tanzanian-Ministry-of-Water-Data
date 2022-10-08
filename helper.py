def explore_column(df, column):
    """
    Helper function for exploring columns.
    
    Args:
          column (str): Column to explore.
          df (dataframe): Dataframe to explore.
    """
    print("null values")
    print(df[column].isnull().sum())
    print("")
    print("value counts")
    print(df[column].value_counts())
    print("")
    print("number of unique values")
    print(df[column].nunique())
    print("")
    print("descriptive statistics")
    print(df[column].describe())

def model_helper(X, y, model, feature_importance = False):
    """
    Helper function to run sklearn models.  
    
    Args:
        X (dataframe): Features to train on. 
        y (series): Target variable
        model (sklearn): Model to train on. 
        feature_importance (bool): True equals plot feature importance table. 
    """
    from sklearn.model_selection import train_test_split
    import pandas as pd

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = .2, random_state = 11)
    model.fit(X_train, y_train)

    print(f"Training Score: {model.score(X_train, y_train)}")
    print(f"Testing Score: {model.score(X_test, y_test)}")
    
    if feature_importance:
        feat_import = pd.DataFrame({"features": X_train.columns, "importance": model.feature_importances_})
        print(feat_import.sort_values("importance", ascending=False))