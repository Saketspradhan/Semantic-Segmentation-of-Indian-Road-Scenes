# Semantic Segmentation of Indian Road Scenes using Unsupervised Domain Adaptation

**Overview**
This paper explores using unsupervised domain adaptation to improve semantic segmentation of Indian road scenes. Semantic segmentation assigns a class label to each pixel in an image and is useful for self-driving cars, traffic monitoring, etc. However, training models for Indian roads are challenging due to variability in conditions and a lack of labeled data.

**Methods**
Two models have been implemented and tested, namely, SegFormer and DAFormer. Both use encoder-decoder architectures based on transformers to output dense pixel predictions.

SegFormer uses a hierarchical transformer encoder and simple MLP decoder to output multi-scale features.
DAFormer is optimized for unsupervised domain adaptation using a transformer encoder and context-aware feature fusion decoder.

**Experiments**
The models are evaluated on Indian and standard datasets like Cityscapes, GTA5, and SYNTHIA. 

DAFormer outperforms other methods, achieving:

| DAFormer | mIoU |
|-|-| 
| Cityscapes | 95.7% |
| SYNTHIA | 84.5% |
| National Dataset for Indian Roads | 90.8% |

| Model | Cityscapes mIoU | SYNTHIA mIoU | 
|-|-|-|  
| SegFormer | 95.7% | 84.5% |
| DAFormer | 96.4% | 85.2% |

**Conclusion**
Unsupervised domain adaptation is promising for semantic segmentation of complex Indian road scenes. DAFormer adapts better to target datasets and surpasses other architectures. More research is needed to handle varying conditions.
