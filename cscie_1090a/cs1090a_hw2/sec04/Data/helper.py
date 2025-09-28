import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def polynomial_regression_helper(scaled_train_df, 
                                 scaled_test_df, 
                                 ohe_train_df, 
                                 ohe_test_df,
                                 y_train,
                                 y_test,
                                 poly_deg_list=[1, 2, 3, 4]):
  """Generate polynomial terms based on polynomial degrees and fit linear
  regression model on the data (original terms + polynomial terms + categorical 
  terms) and see the effect of model complexity on train score and test score.

    Args:
        scaled_train_df: Scaled train x (nuemrical variables).
        scaled_test_df: Scaled test x (nuemrical variables).
        ohe_train_df: One hot encoded train x (categorical variables).
        ohe_test_df: One hot encoded test x (categorical variables).
        y_train: train y.
        y_test: test y.
        poly_deg_list: list of poly degrees to assess.

    Returns:
        None.

    """
  
  # List to store model scores
  train_r2 = []
  test_r2 = []

  fig = plt.figure()
  
  # For each polynomial degree
  for poly_deg in poly_deg_list:

    # Generate the polynomial terms from existing numerial variables
    poly = PolynomialFeatures(degree=poly_deg,
                              interaction_only=False, # the default
                              include_bias=False)
    poly_train = poly.fit_transform(scaled_train_df)
    poly_test = poly.transform(scaled_test_df)

    # Convert data to pd.Dataframe
    poly_train_df = pd.DataFrame(poly_train, columns=poly.get_feature_names_out())
    poly_test_df = pd.DataFrame(poly_test, columns=poly.get_feature_names_out())
    
    # Include one hot encoded categorical variables
    design_train_df = pd.concat([poly_train_df, ohe_train_df], axis=1)
    design_test_df = pd.concat([poly_test_df, ohe_test_df], axis=1)

    # Linear regression
    linreg = LinearRegression().fit(design_train_df, y_train)
    train_r2.append(linreg.score(design_train_df, y_train)) # R^2
    test_r2.append(linreg.score(design_test_df, y_test))

  # Plot the effect of model complexity on train and test score
  plt.plot(poly_deg_list, train_r2, label=r'Train $R^2$')
  plt.plot(poly_deg_list, test_r2, label=r'Test $R^2$')
  plt.xlabel(f'Poly Degree')
  plt.ylabel(f'$R^2$')
  plt.legend()

  # Zoomed in
  inset_ax = fig.add_axes([0.35, 0.35, 0.3, 0.3]) # [left, bottom, width, height] in figure coordinates
  inset_ax.plot(poly_deg_list, train_r2) # Zoomed-in portion
  inset_ax.plot(poly_deg_list, test_r2)
  inset_ax.set_ylim([0.65, 0.9])
  inset_ax.set_title('Zoomed In')



def reorganize_regions(row):
  """From on the region and nationality in the row, return the updated regions
  for nationalities such as England, Wales, Argentina, Cameroon, and USA.

  Args:
      row: a row of a dataframe containing `region` and `nationality` features
  Returns:
      an integar corresponding to the correct region.

  """

  # Get current region and nationality.
  region = row.region
  nationality = row.nationality

  match nationality:
    # Moving England and Wales to region 1.
    case 'England' | 'Wales': return 1
    # Moving Argentina to region 3.
    case 'Argentina': return 3
    # Moving Cameroon to region 4.
    case 'Cameroon': return 4
    # Moving United States to region 3.
    case 'United States': return 3
    # For all other nationality, keep at original region.
    case _: return region
