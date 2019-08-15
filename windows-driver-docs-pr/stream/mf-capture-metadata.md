# Capture Stats Metadata Attributes

The table below summarizes the available capture stats IMFAttributes for
MFT0 for preview, video, and still capture.

The capture stats listed for still is mandatory for every photo captured
except MF\_CAPTURE\_METADATA\_FLASH\_POWER which is dependent on
driver’s capability. The capture stats listed for preview and video
should be delivered as the best effort and the driver may or may not
deliver all capture stats on all frames based on the availability and
performance considerations.

| Name                                            | Type             | Pin                   |
| ----------------------------------------------- | ---------------- | --------------------- |
| MF\_CAPTURE\_METADATA\_FOCUSSTATE               | UINT32           | Preview               |
| MF\_CAPTURE\_METADATA\_FACEROIS                 | Blob             | Preview, Video        |
| MF\_CAPTURE\_METADATA\_EXPOSURE\_TIME           | UINT64           | Preview, Still        |
| MF\_CAPTURE\_METADATA\_EXPOSURE\_COMPENSATION   | Blob             | Preview, Still        |
| MF\_CAPTURE\_METADATA\_ISO\_SPEED               | UINT32           | Preview, Still        |
| MF\_CAPTURE\_METADATA\_LENS\_POSITION           | UINT32           | Preview, Still        |
| MF\_CAPTURE\_METADATA\_SCENE\_MODE              | UINT64           | Still                 |
| MF\_CAPTURE\_METADATA\_FLASH                    | UINT32 (Boolean) | Preview, Still        |
| MF\_CAPTURE\_METADATA\_FLASH\_POWER             | UINT32           | Still                 |
| MF\_CAPTURE\_METADATA\_WHITEBALANCE             | UINT32 (Kelvin)  | Preview, Still        |
| MF\_CAPTURE\_METADATA\_ZOOMFACTOR               | UINT32 (Q16)     | Still                 |
| MF\_CAPTURE\_METADATA\_ISO\_GAINS               | Blob             | Preview               |
| MF\_CAPTURE\_METADATA\_SENSORFRAMERATE          | UINT64           | Preview               |
| MF\_CAPTURE\_METADATA\_WHITEBALANCE\_GAINS      | Blob             | Preview               |
| MF\_CAPTURE\_METADATA\_FACEROITIMESTAMPS        | Blob             | Preview, Video        |
| MF\_CAPTURE\_METADATA\_FACEROICHARACTERIZATIONS | Blob             | Preview, Video        |
| MF\_CAPTURE\_METADATA\_HISTOGRAM                | Blob             | Preview               |
| MF\_CAPTURE\_METADATA\_FRAME\_ILLUMINATION      | UINT64           | IR Pin used for Hello |

## MF_CAPTURE_METADATA_FOCUSSTATE

MF\_CAPTURE\_METADATA\_FOCUSSTATE attribute contains the current focus
state which can take one of the following values.

typedef enum

{

KSCAMERA\_EXTENDEDPROP\_FOCUSSTATE\_UNINITIALIZED = 0,

KSCAMERA\_EXTENDEDPROP\_FOCUSSTATE\_LOST,

KSCAMERA\_EXTENDEDPROP\_FOCUSSTATE\_SEARCHING,

KSCAMERA\_EXTENDEDPROP\_FOCUSSTATE\_FOCUSED,

KSCAMERA\_EXTENDEDPROP\_FOCUSSTATE\_FAILED,

} KSCAMERA\_EXTENDEDPROP\_FOCUSSTATE;

## MF_CAPTURE_METADATA_FACEROIS

MF\_CAPTURE\_METADATA\_FACEROIS attribute contains the face rectangle
info detected by the driver. By default driver\\MFT0 should provide the
face info on preview stream. If driver advertises the capability on
other streams, driver\\MFT must provide the face info on the
corresponding streams if the application enables face detection on those
streams. When video stabilization is enabled on driver, the face info
should be provided post the video stabilization. The data structures
below describe the blob format for MF\_CAPTURE\_METADATA\_FACEROIS. The
dominate face must be the first FaceRectInfo in the blob.

typedef struct tagFaceRectInfoBlobHeader

{

ULONG Size; // Size of this header + all FaceRectInfo following

ULONG Count; // Number of FaceRectInfo’s in the blob

} FaceRectInfoBlobHeader;

typedef struct tagFaceRectInfo

{

RECT Region; // Relative coordinates on the frame that face detection is
running (Q31 format)

LONG ConfidenceLevel; // Confidence level of the region being a face
(\[0, 100\])

} FaceRectInfo;

Note that FaceRectinfoBlobHeader and FaceRectInfo structs only describe
the blob format for the MF\_CAPTURE\_METADATA\_FACEROIS attribute. The
metadata item structure for face ROIs (KSCAMERA\_METADATA\_ITEMHEADER +
face ROIs metadata payload) is up to driver and must be 8-byte aligned.

By design, if a stream is configured with face detection enabled and the
scene in question does not contain any faces during capture, the driver
is still required to attach a “dummy” MF\_CAPTURE\_METADATA\_FACEROIS
attribute to each sample which has no face information associated with
it. (A “dummy” face ROI attribute has the *Count* field of the
*FaceRectInfoBlobHeader* structure set to zero.)

## MF_CAPTURE_METADATA_EXPOSURE_TIME

MF\_CAPTURE\_METADATA\_EXPOSURE\_TIME attribute contains the exposure
time applied to the sensor when preview and\\or photo frame was captured
which is a UINT64 and is in 100ns.

## MF_CAPTURE_METADATA_EXPOSURE_COMPENSATION

MF\_CAPTURE\_METADATA\_EXPOSURE\_COMPENSATION attribute contains an EV
compensation step flag and an EV Compensation value in units of the step
applied to the sensor when preview and\\or photo frame was captured.

The data structure below describes the blob format for
MF\_CAPTURE\_METADATA\_EXPOSURE\_COMPENSATION.

typedef struct tagCapturedMetadataExposureCompensation

{

UINT64 Flags; // KSCAMERA\_EXTENDEDPROP\_EVCOMP\_XXX step flag

INT32 Value; // EV Compensation value in units of the step

} CapturedMetadataExposureCompensation;

Note that CapturedMetadataExposureCompensation struct only describes the
blob format for the MF\_CAPTURE\_METADATA\_EXPOSURE\_COMPENSATION
attribute. The metadata item structure for EV compensation
(KSCAMERA\_METADATA\_ITEMHEADER + EV compensation metadata payload) is
up to driver and must be 8-byte aligned.

## MF_CAPTURE_METADATA_ISO_SPEED

MF\_CAPTURE\_METADATA\_ISO\_SPEED attributes contains the ISO speed
value applied to the sensor when preview and\\or photo frame was
captured. This is unitless.

## MF_CAPTURE_METADATA_LENS_POSITION

MF\_CAPTURE\_METADATA\_LENS\_POSITION attribute contains the logical
lens position when preview and\\or photo frame was captured, which is
unitless. This is the same value that can be queried from
KSPROPERTY\_CAMERACONTROL\_EXTENDED\_FOCUS in a GET call.

## MF_CAPTURE_METADATA_FLASH

MF\_CAPTURE\_METADATA\_FLASH attribute contains a boolean value when
preview and\\or photo frame was captured, with 1 meaning flash on and 0
meaning flash off.

## MF_CAPTURE_METADATA_SCENE_MODE

MF\_CAPTURE\_METADATA\_SCENE\_MODE attribute contains the scene mode
applied to the photo captured which is a 64bit
KSCAMERA\_EXTENDEDPROP\_SCENEMODE\_XXX flag.

## MF_CAPTURE_METADATA_FLASH_POWER

MF\_CAPTURE\_METADATA\_FLASH\_POWER attribute contains the flash power
applied to the photo captured which is a value in the range of \[0,
100\]. This attribute should be omitted if the driver does not support
adjustable power for flash.

## MF_CAPTURE_METADATA_WHITEBALANCE

MF\_CAPTURE\_METADATA\_WHITEBALANCE attribute contains the white balance
applied to the sensor when preview and\\or photo frame was captured,
which is a value in Kevin.

## MF_CAPTURE_METADATA_ZOOMFACTOR

MF\_CAPTURE\_METADATA\_ZOOMFACTOR attribute contains the zoom value
applied to the photo captured which is the same value that can be
queried from KSPROPERTY\_CAMERACONTROL\_EXTENDED\_ZOOM in a GET call.
This should be in Q16.

## MF_CAPTURE_METADATA_ISO_GAINS

MF\_CAPTURE\_METADATA\_ISO\_GAINS attribute contains the analog and
digital gains applied to the senor when the preview frame was captured.
This is unitless.

The data structure below describes the blob format for
MF\_CAPTURE\_METADATA\_ISO\_GAINS.

typedef struct tagCapturedMetadataISOGains

{

FLOAT AnalogGain;

FLOAT DigitalGain;

} CapturedMetadataISOGains;

Note that CapturedMetadataISOGains struct only describes the blob format
for the MF\_CAPTURE\_METADATA\_ISO\_GAINS attribute. The metadata item
structure for ISO gains (KSCAMERA\_METADATA\_ITEMHEADER + ISO gains
metadata payload) is up to driver and must be 8-byte aligned.

## MF_CAPTURE_METADATA_SENSORFRAMERATE

MF\_CAPTURE\_METADATA\_SENSORFRAMERATE attribute contains the measured
sensor readout rate in hertz when a preview frame is captured, which
consists of a numerator value in the upper 32 bit and a denominator
value in the lower 32 bit.

## MF_CAPTURE_METADATA_WHITEBALANCE_GAINS

MF\_CAPTURE\_METADATA\_WHITEBALANCE\_GAINS attribute contains the white
balance gains applied to R, G, B by the sensor and\\or ISP when the
preview frame was captured. This is a unitless.

The data structure below describes the blob format for
MF\_CAPTURE\_METADATA\_WHITEBALANCE\_GAINS.

typedef struct tagCapturedMetadataWhiteBalanceGains

{

FLOAT R;

FLOAT G;

FLOAT B;

} CapturedMetadataWhiteBalanceGains;

Note that CapturedMetadataWhiteBalanceGains struct only describes the
blob format for the MF\_CAPTURE\_METADATA\_WHITEBALANCE\_GAINS
attribute. The metadata item structure for white balance gains
(KSCAMERA\_METADATA\_ITEMHEADER + white balance gains metadata payload)
is up to driver and must be 8-byte aligned.

## MF_CAPTURE_METADATA_FACEROITIMESTAMPS

MF\_CAPTURE\_METADATA\_FACEROITIMESTAMPS attribute contains the time
stamp info for the face ROIs identified in
MF\_CAPTURE\_METADATA\_FACEROIS. For the device that cannot provide the
time stamp for face ROIs, this attribute should be omitted.

The data structure below describes the blob format for
MF\_CAPTURE\_METADATA\_FACEROITIMESTAMPS.

typedef struct tagMetadataTimeStamps

{

    ULONG Flags; // Bitwise OR of MF\_METADATATIMESTAMPS\_XXX flags

    LONGLONG Device; // QPC time for the sample where the face rect is
derived from (in 100ns)

    LONGLONG Presentation; // PTS for the sample where the face rect is
derived from (in 100ns)

} MetadataTimeStamps;

For Flags field, we will define the following bit flags to indicate
which time stamp is valid. MFT0 must set Flags to
MF\_METADATATIEMSTAMPS\_DEVICE and the appropriate QPC time for Device,
if the driver provides the timestamp metadata for the face ROIs.

\#define MF\_METADATATIMESTAMPS\_DEVICE 0x00000001

\#define MF\_METADATATIMESTAMPS\_PRESENTATION 0x00000002

Note that MetadataTimeStamps struct only describes the blob format for
the MF\_CAPTURE\_METADATA\_FACEROITIMESTAMPS attribute. The metadata
item structure for timestamp (KSCAMERA\_METADATA\_ITEMHEADER + timestamp
metadata payload) is up to driver and must be 8-byte aligned.

## MF_CAPTURE_METADATA_FACEROICHARACTERIZATIONS

MF\_CAPTURE\_METADATA\_FACEROICHARACTERIZATIONS attribute contains the
blink and\\or facial expression state for the face ROIs identified in
MF\_CAPTURE\_METADATA\_FACEROIS.  For the device that doesn’t support
blink and\\or facial expression detection, this attribute should be
omitted.

The data structure below describes the blob format for
MF\_CAPTURE\_METADATA\_FACEROICHARACTERIZATIONS. 

Note that FaceCharacterizationBlobHeader and FaceCharacterization
structs only describe the blob format for the
MF\_CAPTURE\_METADATA\_FACEROICHARACTERIZATIONS attribute. The metadata
item structure for the face characterizations
(KSCAMERA\_METADATA\_ITEMHEADER + face characterizations metadata
payload) is up to driver and must be 8-byte aligned.

typedef struct tagFaceCharacterizationBlobHeader

{

    ULONG Size; // Size of this header + all FaceCharacterization
following

    ULONG Count; // Number of FaceCharacterization’s in the blob. Must
match the number of FaceRectInfo’s in FaceRectInfoBlobHeader

} FaceCharacterizationBlobHeader;

typedef struct tagFaceCharacterization

{

    ULONG BlinkScoreLeft; // \[0, 100\]. 0 indicates no blink for the
left eye. 100 indicates definite blink for the left eye

    ULONG BlinkScoreRight; // \[0, 100\]. 0 indicates no blink for the
right eye. 100 indicates definite blink for the right eye

    ULONG FacialExpression; // Any one of the
MF\_METADATAFACIALEXPRESSION\_XXX defined

    ULONG FacialExpressionScore; // \[0, 100\]. 0 indicates no such
facial expression as identified. 100 indicates definite such facial
expression as defined

} FaceCharacterization;

The following defines the possible facial expression that can be
detected.  

\#define MF\_METADATAFACIALEXPRESSION\_SMILE             0x00000001

If MF\_CAPTURE\_METADATA\_FACEROICHARACTERIZATIONS attribute presents,
the number and the order of FaceCharacterization entries in its blob
must match the number and the order of the FaceRectInfo entries in the
blob of MF\_CAPTURE\_METADATA\_FACEROIS.   Each FaceCharacterization
entry represents the blink and\\or facial expression state of the face
in the corresponding FaceRectInfo entry at the same index.

The figure below illustrates the layouts of a face characterizations
blob and a face ROIs blob of four faces with the first one neither
blinking nor smiling, the second one blinking left eye, the third one
smiling, and the fourth one both blinking (both eyes) and smiling.

## MF_CAPTURE_METADATA_FRAME_ILLUMINATION

MF\_CAPTURE\_METADATA\_FRAME\_ILLUMINATION attribute for IR cameras
specifies whether the frames is using active IR illumination and should
be used in conjunction with
FACEAUTH\_MODE\_ALTERNATIVE\_FRAME\_ILLUMINATION. It is only used for IR
samples and should not be present on RGB frames if the camera supports
both IR and color samples.

Value should be set to 0xXXXXXXXXXXXXXXX1 if frame was captured when
active illumination was on and set to 0xXXXXXXXXXXXXXXX0 if no
illumination was present when capturing the frame.

## MF_CAPTURE_METADATA_HISTOGRAM

MF\_CAPTURE\_METADATA\_HISTOGRAM attribute contains the histogram when a
preview frame is captured. The data structures below describe the blob
format for MF\_CAPTURE\_METADATA\_HISTOGRAM.

typedef struct tagHistogramGrid

{

ULONG Width; // Width of the sensor output that histogram is collected
from

ULONG Height; // Height of the sensor output that histogram is collected
from

RECT Region; // Absolute coordinates of the region on the sensor output
that the histogram is collected for

} HistogramGrid;

typedef struct tagHistogramBlobHeader

{

ULONG Size; // Size of the entire histogram blob in bytes

ULONG Histograms; // Number of histograms in the blob. Each histogram is
identified by a HistogramHeader

} HistogramBlobHeader;

typedef struct tagHistogramHeader

{

ULONG Size; // Size of this header + (HistogramDataHeader + histogram
data following)\*number of channels available

ULONG Bins; // Number of bins in the histogram

ULONG FourCC; // Color space that the histogram is collected from

ULONG ChannelMasks; // Masks of the color channels that the histogram is
collected for

HistogramGrid Grid; // Grid that the histogram is collected from

} HistogramHeader;

typedef struct tagHistogramDataHeader

{

ULONG Size; // Size in bytes of this header + histogram data following

ULONG ChannelMask; // Mask of the color channel for the histogram data

ULONG Linear; // 1, if linear; 0 nonlinear

} HistogramDataHeader;

For ChannelMasks field, we will define the following bitmasks to
indicate the available channels in the histogram.

\#define MF\_HISTOGRAM\_CHANNEL\_Y 0x00000001

\#define MF\_HISTOGRAM\_CHANNEL\_R 0x00000002

\#define MF\_HISTOGRAM\_CHANNEL\_G 0x00000004

\#define MF\_HISTOGRAM\_CHANNEL\_B 0x00000008

\#define MF\_HISTOGRAM\_CHANNEL\_Cb 0x00000010

\#define MF\_HISTOGRAM\_CHANNEL\_Cr 0x00000020

Notes:

1.  Each blob can contain multiple histograms collected from different
    regions or different color spaces of the same frame

2.  Each histogram in the blob is identified by its own HistogramHeader

3.  Each histogram has its own region and sensor output size associated.
    For full frame histogram, the region will match the sensor output
    size specified in HistogramGrid.

4.  Histogram data for all available channels are grouped under one
    histogram. Histogram data for each channel is identified by a
    HistogramDataHeader immediate above the data. ChannelMasks indicate
    how many and what channels are having the histogram data, which is
    the bitwise OR of the supported MF\_HISTOGRAM\_CHANNEL\_XXX bitmasks
    as defined above. ChannelMask indicates what channel the data is
    for, which is identified by any one of the
    MF\_HISTOGRAM\_CHANNEL\_XXX bitmasks defined above.

The figure below illustrates the layout of a histogram blob with a full
frame Y-only histogram.

Histogram data is an array of ULONG with each entry representing the
number of pixels falling under a set of tonal values as categorized by
the bin. The data in the array should start from bin 0 to bin N-1, where
N is the number of bins in the histogram, i.e.,
HistogramBlobHeader.Bins.

The figure below illustrates the layout of the histogram data section.

The figure below illustrates the layout of a histogram blob with a
full-frame YRGB histogram with four channels.

The figure below illustrates the layout of a histogram blob with a
Y-only histogram followed by a RGB histogram with three channels.

For Threshold, at minimum a full frame histogram with Y channel must be
provided which should be the first histogram in the histogram blob, if
KSPROPERTY\_CAMERACONTROL\_EXTENDED\_HISTOGRAM is supported.

Note that HistogramBlobHeader, HistogramHeader, HistogramDataHeader and
Histogram data only describe the blob format for the
MF\_CAPTURE\_METADATA\_HISTOGRAM attribute. The metadata item structure
for the histogram (KSCAMERA\_METADATA\_ITEMHEADER + all histogram
metadata payload) is up to driver and must be 8-byte aligned.

# Histogram Metadata Control 

KSPROPERTY\_CAMERACONTROL\_EXTENDED\_HISTOGRAM is a property ID that
will be used to control the histogram metadata produced by the driver.
This is a pin level control for preview pin only and is defined as
following:

\#if (NTDDI\_VERSION \>= NTDDI\_WIN8)

typedef enum {

…

KSPROPERTY\_CAMERACONTROL\_EXTENDED\_HISTOGRAM

} KSPROPERTY\_CAMERACONTROL\_EXTENDED\_PROPERTY;

For KSCAMERA\_EXTENDEDPROP\_HEADER, we will define the following bit
flags to control the histogram metadata in driver. The default is OFF.

\#define KSCAMERA\_EXTENDEDPROP\_HISTOGRAM\_OFF 0x0000000000000000

\#define KSCAMERA\_EXTENDEDPROP\_HISTOGRAM\_ON 0x0000000000000001

This control must be used before the
KSPROPERTY\_CAMERACONTROL\_EXTENDED\_METADATA control to ensure the
proper sized metadata buffer is allocated.

If set to HISTOGRAM\_OFF, the driver shall not deliver the histogram
metadata on preview pin. The driver should not include the histogram
metadata size in its metadata buffer size requirement.

If set to HISTOGRAM\_ON, the driver shall deliver the histogram metadata
on preview pin. The driver must include the histogram metadata size in
its metadata buffer size requirement.

If the driver does not have the capability to produce histogram
metadata, the driver should not implement this control. If the driver
supports this control, it must also support
KSPROPERTY\_CAMERACONTROL\_EXTENDED\_METADATA control.

The SET call of this control has no effect when the preview pin is inany
state higher than the KSSTATE\_STOP state. The driver shall reject the
SET call received if preview is not in the stop state and returns
STATUS\_INVALID\_DEVICE\_STATE. In a GET call, driver should return the
current settings in Flags field.

This is a synchronous control. There are no capabilities defined for
this control.

## KSCAMERA_EXTENDEDPROP_HEADER

**Version**

> Must be 1.

**PinId**

> Must be the Pin ID associated with the preview pin.

**Size**

> Must be sizeof(KSCAMERA\_EXTENDEDPROP\_HEADER)+
> sizeof(KSCAMERA\_EXTENDEDPROP\_VALUE)

**Result**

> Indicates the error results of the last SET operation. If no SET
> operation has taken place, this must be 0.

**Capability**

> Must be 0.

**Flags**

> This is a read/write field. This can be any one of the
> KSCAMERA\_EXTENDEDPROP\_HISTOGRAM\_XXX flags defined above.

## KSCAMERA\_EXTENDEDPROP\_VALUE

Not used
