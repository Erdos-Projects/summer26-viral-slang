# Project: Early Signal Detection of Viral Internet Slang

## 1. Problem Definition

* **The Question:** Can we predict if a specific word token will cross the 99th percentile of relative usage frequency within a 7-day window?

* **Decision Impact:** This analysis informs how social media platforms and brand marketers identify emerging cultural trends before they reach saturation.

* **Unit of Analysis:** A unique, clustered word token observed over a specific 24-hour window.

* **Scope & Boundaries:** Analysis is limited to English-language text from selected subreddits; time horizon is restricted to the available Kaggle historical data.

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

4. **Authentication (Mandatory):**
   Because we do not commit secret API keys, you must create a `.env` file in the root directory.

   * Download your `kaggle.json` from your Kaggle account settings.

   * Create a `.env` file and add your credentials:

   ```text
   KAGGLE_USERNAME=your_username_here
   KAGGLE_KEY=your_alphanumeric_key_here
   ```

## 3. Data Acquisition

We are currently using a Kaggle dataset as our primary source while Reddit API approvals are pending.

* **Source Identifier:** `pavellexyr/the-reddit-dataset-dataset`.

* **Provenance:** Data is pulled via the official Kaggle API; scripts log timestamps and download status to `/logs`.

* **Execution:**
  Run the following script to download and unzip the raw CSV directly into your local `data/raw/` folder:

  ```bash
  python src/data/load_kaggle_data.py
  ```

## 4. Ethical & Legal Considerations

* **Licensing:** This project adheres to the Kaggle dataset's specific license and Reddit's User Agreement.

* **Privacy:** No Personally Identifiable Information (PII) is included in the modeling; we analyze aggregated word tokens, not individual users.

## 5. Preliminary KPIs (Key Performance Indicators)

We evaluate success using the following metrics to account for the highly imbalanced nature of viral events:

| Metric | Type | Purpose | 
| ----- | ----- | ----- | 
| **F1-Score** | Primary | Balances precision and recall for the "Viral" class. | 
| **ROC-AUC** | Primary | Evaluates the model's ability to distinguish between duds and breakouts. | 
| **Precision** | Secondary | Measures how many flagged words actually went viral (minimizing false alarms). | 
| **Recall** | Secondary | Measures how many actual viral trends the model successfully caught. | 

## 6. Baseline Modeling

All baseline experiments are recorded in `notebooks/baseline.ipynb`.

* **Baseline Models:** `DummyClassifier`, `LogisticRegression`, and `RandomForestClassifier`.

* **Validation:** All baselines are evaluated using 5-fold cross-validation (`KFold`) to ensure learnability.