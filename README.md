# Project: Early Signal Detection of Viral Internet Slang

Alejandro Vargas-Altamirano
Hargun Bhatia
Jameson Auger
Karthik Srinivasan
Yasir Khan

## 1. Problem Definition

* **The Question:** Can we predict if a specific word token will go viral over the next 3 weeks, which for this project is defined as the relative frequency of the word's usage doubling compared to a baseline.

* **Decision Impact:** This analysis informs how social media platforms and brand marketers identify emerging cultural trends before they reach saturation.

* **Unit of Analysis:** A unique, clustered word token observed over a 20 week window

* **Scope & Boundaries:** Analysis is limited to English-language text from selected Youtube channel's comment sections. For this project all of the chosen channels are gaming focused.

* **Anti-Goals:** This project will **not** address live real-time stream processing, sentiment analysis of the slang, or a front-end dashboard.

## 2. Environment Setup

To ensure reproducibility across all team members, we use a strict environment specification.

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/karthik-yale/EarlySlangDetection.git
   cd EarlySlangDetection
   ```

2. **Create and Activate a Conda Environment:**
   It is highly recommended to use Conda to manage your virtual environment and isolate project dependencies.

   ```bash
   conda create --name slang-env python=3.13 -y
   conda activate slang-env
   ```

3. **Install Dependencies:**
   Once your Conda environment is active, use `pip` to install the requirements directly into it:

   ```bash
   pip install -r requirements.txt
   ```


## 3. Data Acquisition

Data was collected from Youtube using the Youtube Data API v3. The dataset includes the top 100 comments (by likes) from the most recent n videos from a particular channel, where n varies based on channel, but is often around 500 videos.

The specific data collected was the text of the comment, the number of likes the comment received, the date the comment was published, the video id, and the name of the channel the video was on.

## 4. Ethical & Legal Considerations

* **Licensing:** This project adheres to the Youtube API Terms of Service

* **Privacy:** No Personally Identifiable Information (PII) is included in the modeling; we analyze aggregated word tokens, not individual users.

## 5. Preliminary KPIs (Key Performance Indicators)

We evaluate success using the following metrics to account for the highly imbalanced nature of viral events. The first four are used to evaluate the models for regression (estimating the change in relative frequency), and the next four are for classification (will a word more than double in relative frequency).


* **Root Mean Squared Error**
* **R^2**
* **Spearman Correlation**
* **Pearson Correlation**

* **F1-Score** 
* **ROC-AUC**
* **Precision**
* **Recall**

## 6. Folder Structure

\src\ - All Python scripts and Jupyter Notebooks

--\EDA\ - All exploratory data analysis

--\Experimental Models\ - Two attempts at modeling that had promising results but did not become our final maodel

--\Final Model\ - out final model, including the hyperparameter tuning and comparison against other models that lead to it


\data\ - All raw data used in the project

\Output\ - Graphs and figures created from Jupyter notebooks from src that were found to be important or were used in the presentation.
