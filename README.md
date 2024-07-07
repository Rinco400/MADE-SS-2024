# Jayvee Exercise Badges

![](https://byob.yarr.is/Rinco400/MADE-SS-2024/score_ex1) ![](https://byob.yarr.is/Rinco400/MADE-SS-2024/score_ex2) ![](https://byob.yarr.is/Rinco400/MADE-SS-2024/score_ex3) ![](https://byob.yarr.is/Rinco400/MADE-SS-2024/score_ex4) ![](https://byob.yarr.is/Rinco400/MADE-SS-2024/score_ex5)

# Methods of Advanced Data Engineering Jayvee Exercise & Python Pipeline Project


## Project Work
# Analysis of Radioactivity in Baby Food and Natural Mineral Water Quality

## Main Question
How do the levels of radioactivity in baby food compare with the quality parameters of natural mineral water, and what are the potential correlations and implications for public health and environmental quality?

<img src="project\pictures\Radioactivity.png" width="800" height="466">

## Project Overview
This project aims to conduct a comprehensive analysis of radioactivity levels in baby food ("Babynahrung Gemüse und Hühnchen mit Nudeln") and compare these findings with the quality parameters of natural mineral water within the Hamburg region. By investigating trends over time and across different locations within Hamburg, the study seeks to uncover potential correlations and provide insights into the factors influencing both food and water quality. The findings will contribute to understanding environmental quality and public health implications, guiding future measures for quality management in Hamburg.

### Datasets
## Datasource 1:govdata.de
* Metadata URL 1: https://www.govdata.de/ckan/dataset/messergebnisse-zur-radioaktivitat-in-natural-mineralwater-13-03-2024.rdf
* Data URL 1: https://daten.transparenz.hamburg.de/Dataport.HmbTG.ZS.Webservice.GetRessource100/GetRessource100.svc/f565c684-2c98-4c61-982d-c1ec7ec2cade/Natural_Mineralwater.csv
* Data Type: CSV
* Data of Measurement results for radioactivity in: Natural Mineralwater.

## Datasource 2:govdata.de
* Metadata URL 1: https://www.govdata.de/ckan/dataset/messergebnisse-zur-radioaktivitat-in-babynahrung-gemuse-und-huhnchen-mit-nudeln-13-03-2024.rdf
* Data URL 1: https://daten.transparenz.hamburg.de/Dataport.HmbTG.ZS.Webservice.GetRessource100/GetRessource100.svc/fa8ce806-e088-4bfb-9aa8-87c5c61807b1/Babynahrung_Gemuese_und_Huehnchen_mit_Nudeln.csv
* Data Type: CSV
* Measurement results for radioactivity in: Baby food vegetables and chicken with noodles.

## Installation and Usage
Instructions for setting up the project environment and running the analysis scripts.

```bash
# Clone the repository
git clone https://github.com/Rinco400/MADE-SS-2024.git

# Install dependencies
pip install -r requirements.txt

```

## Tools and Technologies Used
- Data Analysis: Python (Pandas,Numpy)
- Visualization: Matplotlib, Seaborn
- Version Control: Git, GitHub

[**Project Data Report**](project/data-report.pdf): Detailed documentation on data cleaning and pipeline procedures.

[**Project Analysis Report**](project/analysis-report.pdf): Comprehensive final report featuring data analysis and visualizations.

[**Project Visualization**](project/pipeline_compare.ipynb): Jupyter Notebook demonstrating exploratory data analysis (EDA) for 
the project.

[**Presentation Slides**](project/slides.pdf)

[**Presenation Video Link**](project/presentation-video.md)

## Data Pipeline and Testing

### Automated Data Pipeline
Discover the script [here](project/pipeline.py).

Our project employs an automated data pipeline tailored for wildfire analysis, comprising the following steps:

1. **Data Retrieval**: Monthly wildfire burned area and emission datasets are automatically fetched from specified sources.
2. **Data Processing**: Essential transformations and cleaning processes are applied to ensure data accuracy and consistency.
3. **Data Integration**: The processed data is loaded into structured formats, making it ready for detailed analysis.

This pipeline guarantees that our wildfire data is consistently accurate and prepared for in-depth trend and impact analysis.

### Testing Script
Explore the script [here](project/test.py).

To ensure the integrity of our wildfire data pipeline, we've developed a comprehensive testing script that includes:

1. **Verification of Data Retrieval**: Ensures that data is accurately fetched from the sources.
2. **Validation of Data Processing**: Confirms that cleaning and transformation processes are correctly applied.
3. **Integrity Assurance**: Maintains data consistency and accuracy throughout the pipeline.

### Continuous Integration Workflow
View the workflow configuration [here](.github/workflows/project-test.yml).

To maintain the robustness of our data pipeline, we utilize an automated workflow via GitHub Actions:

- **Continuous Integration (CI)**: The testing script is triggered automatically with every push to the main branch. This ensures that any updates or changes do not disrupt the pipeline's functionality and accuracy.

Our CI workflow ensures a reliable, error-free approach to analyzing wildfire trends and impacts, delivering high-quality outcomes for the project.

## How to Run the Data Pipeline and Tests
Provide detailed instructions on how to execute the data pipeline and run the test scripts. Include any necessary commands or steps to set up the environment.

```bash
# command to run the data pipeline
python3 project/pipeline.py

# command to execute the test script
python3 project/test.py
```
## Contributing
We welcome contributions to this project! If you would like to contribute, please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourContribution`).
3. Make your changes and commit them (`git commit -am 'Add Data'`).
4. Push to the branch (`git push origin feature/YourContribution`).
5. Create a new Pull Request &
6. Focus Data Limitations.

Please ensure your code is well-documented.

## Limitations

### Data Limitations:

- **Missing Data**: The datasets had instances of missing values marked as 'n.n.', which were replaced with zeros. This imputation could potentially skew the results, as zero may not accurately reflect the true missing values.
- **Data Consistency**: There might be inconsistencies in the data collection methods and reporting standards across the different datasets. These variations can introduce biases and affect the comparability of the results.

### Result Limitations:

- **Limited Variables**: The analysis primarily focused on the 'Ergebnis' column for both datasets. This may not capture all the relevant aspects of food and water quality, thus limiting the comprehensiveness of the findings.
- **Temporal Scope**: The analysis of temporal trends was constrained by the availability and completeness of data over time. Incomplete or sparse time-series data could hinder the identification of long-term trends and patterns, thereby limiting the depth of the temporal analysis.

These limitations highlight the need for more comprehensive and consistent data collection practices and the inclusion of additional relevant variables to enhance the robustness and reliability of future analyses.


## Authors and Acknowledgment
This project was initiated and completed by As Am Mehedi Hasan. 

## Special Thanks to Our Tutors:
I would like to extend my gratitude to our tutors **Philip Heltweg** and **Georg Schwarz**, as well as the **Friedrich-Alexander-Universität Erlangen-Nürnberg (FAU) MADE(Methods of Advanced Data Engineering) team**, for their guidance and support throughout this project.


## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
