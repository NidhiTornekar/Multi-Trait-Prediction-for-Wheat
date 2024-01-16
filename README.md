This project aims to predict the breeding values of various phenotypic traits such as the Grain Filling Duration(GFD), Days to Heading(DH), Plant Height(PH) and Grain Weight per Spike(GWPS) for Indian Wheat(Triticum aestivum L.); given as input the allele sequence of the plant. 

![image](https://github.com/NidhiTornekar/Multi-Trait-Prediction-for-Wheat/assets/121748841/450a6e2d-5e98-43ae-bed0-3a88f3ce4f6e)

The input dataset consisted of two csv files:
One file containing the phenotypic values for 280 genotypes for GWPS-Grain Weight Per Spike(gram), PH-Plant Height(cm), GY-Grain Yield(gram) from five different locations(Dharwad, Delhi, Jharkhand, Karnal, Ludhiana), DH-Days to Heading(days) and GFD-Grain Filling Duration(days) from four different locations(Dharwad, Delhi, Jharkhand, Karnal), and GNPS-Grain Number Per Spike(number) from two different locations(Dharwad, Jharkhand) along with their pooled values.
The second csv file contains the processed SNP genotypic information obtained through Axiom Wheat Breeder’s Genotyping Array. It has 14790 SNPs and corresponding pair of alleles for all the genotypes, along with mention of primary allele/ secondary allele , chromosome (1A-7D), etc.

It can be obtained from:
https://datadryad.org/stash/landing/show?id=doi%3A10.5061%2Fdryad.c866t1g9b

Appropriate data preprocessing was applied, which included encoding and finding correlation between the SNPs and the phenotypic traits. Only pooled traits were considered.

Then, Random Forest was used. This model is stored in the random_forest_model_means.joblib file, and can be loaded in the Flask code to make predictions directly.



Folder structure:
There are two html pages in the templates folder:
The index.html is the home page where user can enter the input allele sequence.
The predict.html page is used to display corresponding phenotypic values.
app.py contains required Flask code to import the joblib model, make predictions and render the results.


To run the project:
Use app.py command.This starts the application in localhost:5000 .
Enter the input allele sequence, click on predict button to navigate to the predictions page.
