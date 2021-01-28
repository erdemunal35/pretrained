# pretrained

Tool to query tensorflowhub and pytorch hub and other repos for pretrained weights for a given architecture or keyword

- https://tfhub.dev/s?q=resnet
- https://github.com/pytorch/hub
- [pretrainedmodels](https://github.com/cadene/pretrained-models.pytorch)

The tool could work like this to query for available weights:

``` shell
$ pretrained search resnet
PNASNet-5-Large [cadene/pretrained-models]
NASNet-A-Large [cadene/pretrained-models]
imagenet/resnet_v2_50/feature_vector [tfhub.dev]
...
# or query for a type of network
$ pretrained search classification
PNASNet-5-Large [cadene/pretrained-models]
NASNet-A-Large [cadene/pretrained-models]
...
```

In order to use the weights, one could think of something like this:

``` shell
#download the pretrained model to the local directory
$ pretrained install PNASNet-5-Large
#download the pretrained model to the directory at /tmp/mymodel
$ pretrained install -o /tmp/mymodel PNASNet-5-Large
```

## Ideas

This repo could be an insertion for [pretrainedmodels](https://github.com/cadene/pretrained-models.pytorch) even though the repo appears stale for about a year. However, it could be an independent project as well.
