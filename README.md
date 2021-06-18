# Bucki


## The idea
Bucki is an API Rest that allows you to record and access data taken in the field. Each campaign is stored into a "bucki," the basic unit for data and metadata storage. You can control the persons who can access your buckis.

We want to ensure that:

- [ ] Data distribution — data should cover all or most of the possible spectrum of the input
- [ ] Data coverage — every class should have enough representation in the dataset
- [ ] Data accuracy — data should be highly relevant to the task in hand and be as close as possible to that used for inference, in terms of quality, format, etc.
- [ ] Feature engineered — data should enable the ML model to learn what we intend it to learn (appropriate features)
- [ ] Data transformation — almost always data acquired cannot be used as-is and an appropriate data transformation pipeline can simplify the model architecture
- [ ] Data volume — depending on whether the ML model is built from scratch or learning transferred from another model, the availability of data is critical
- [ ] Data split — typically data is split into 3 chunks: training (75%), validation (15%) & test (10%) and it’s important to ensure there is no ‘duplicate/same’ data across these chunks and the samples are distributed properly


# Bucki SIS
BuckiSIS is the spectral layer of this project. BuckiSIS acts as a Spectral Information System (SIS) designed to hold spectral campaign data obtained by spectral devices, such as multispectral imaging systems mounted over drones. The inclusion of rich metadata ensures the durability of spectral data, enables the sharing of spectral data between research groups, and makes it possible to implement several ai-based solutions for the real world.

# Spectral data

# Workflow

# RestAPI


## References:
- https://specchio.ch/
- https://www.dji.com/p4-multispectral
- https://www.djangoproject.com/
- https://www.django-rest-framework.org/
- https://12factor.net/

### Another resources you may enjoy

- https://omdena.com/blog/satellite-imagery-dataset/
