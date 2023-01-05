# BMD_prediction
BMD(bone mineral density) prediction in CT images based on deep residual CNN + XAI Analysis
  
Prediction of bone mineral density in CT using deep learning with explainability (Accepted on Dec.2022, Frontiers in Physiology)

## Workflow
![workflow](/readme-figure/workflow.png)
  
## L1 Segmentation
In order to investigate which area had a great impact on the prediction of BMD, we divided the experiment into three cases.  
* ``Case 1 : cropped images``  
* ``Case 2 : entire-vertebrae-masked images``  
* ``Case 3 : vertebral-body-masked images``  
  
U-Net-based model was applied to segment the L1 region.  
  

## BMD Prediction
Deep resiudal CNN for BMD estimation.  

We achieved a maximum correlation coefficient of 0.905 for the test set.  
  
**Estimation Network**  

![prediction](/readme-figure/prediction.png)
  

**Estimation Result**  

![pred_result](/readme-figure/prediction_result.png)



## XAI Interpretation
Grad-CAM is well-known XAI technique used to investigate the attention of a DL network toward an image.  
  
We modified Grad-CAM for this study because it is specialized in a classifer, whereas our network is an estimator (regressor).  
  
![xai](/readme-figure/xai.png)    
 
