---
title: Supporting Dynamic Format Changes in AVStream Codecs
author: windows-driver-content
description: Supporting Dynamic Format Changes in AVStream Codecs
MS-HAID:
- 'shed\_dg\_df628630-aad1-4c20-9580-24aaee621d8c.xml'
- 'stream.supporting\_dynamic\_format\_changes\_in\_avstream\_codecs'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: ae222512-fd19-404a-aaf8-6fbfa2a3349e
keywords: ["hardware codec support WDK AVStream , dynamic format change", "supporting dynamic format change WDK AVStream", "dynamic format change WDK AVStream", "AVStream hardware codec support WDK , supporting dynamic format change"]
---

# Supporting Dynamic Format Changes in AVStream Codecs


When a dynamic format change occurs in a running media stream, the system-supplied Devproxy module negotiates with the capture pin to determine whether the new format will be acceptable.

The following sequence of events occurs when a dynamic format change originates from the media source:

1.  The driver receives a [**KSPROPERTY\_CONNECTION\_PROPOSEDATAFORMAT**](https://msdn.microsoft.com/library/windows/hardware/ff565107) request to determine whether the input KS pin supports the new media type. Drivers must support this property.

2.  If the input pin supports the new media type, the KSPROPERTY\_CONNECTION\_PROPOSEDATAFORMAT handler should return STATUS\_SUCCESS. The driver then determines whether it can resume the stream by using the proposed input together with currently selected output media types. If yes, the stream resumes.

3.  If the input pin does not support the newly proposed media type, the KSPROPERTY\_CONNECTION\_PROPOSEDATAFORMAT handler should return an error. The HW MFT then renegotiates media type with the connected component.

4.  If the input pin supports the new media input type but the KS filter requires a different output media type, the driver should generate a [**KSEVENT\_DYNAMIC\_FORMAT\_CHANGE**](https://msdn.microsoft.com/library/windows/hardware/ff561849) event, as detailed later in this topic, to notify the HW MFT about the media type change.

5.  When the HW MFT receives the KSEVENT notification, it transitions the output pin from **KSSTATE\_RUN** to KSSTATE\_STOP.

6.  The HW MFT then queries the driver for available media types, which translates into a call to the driver's [*AVStrMiniIntersectHandlerEx*](https://msdn.microsoft.com/library/windows/hardware/ff556326) intersection handler. The driver should report preferred output media types in the order of preference.

7.  The user-mode client selects a media type and sets the new media type on the output pin of the HW MFT. This results in a call to the driver's [*AVStrMiniPinSetDataFormat*](https://msdn.microsoft.com/library/windows/hardware/ff556355) dispatch routine. If the driver accepts the format by returning STATUS\_SUCCESS, streaming resumes with the new media type. If the call fails, the components involved in the format change must renegotiate media type.

8.  The HW MFT checks if there is any change in the connected medium. If there is no change, it sets the selected media type on the pin and puts it into KSSTATE\_RUN. If there is a change in the connected medium, the HW MFT destroys the pin and recreates it with the newly selected media type and medium. The MFT then puts the pin into KSSTATE\_RUN.

9.  Streaming resumes.

In certain situations, a media source might not detect a format change. For example, an MPEG2 decoder would have to decode each packet to find any format change.

In such a case, if the driver detects a format change, the hardware driver should generate a dynamic format change KSEVENT. The HW MFT then queries the pin for its supported media types. The pin should return the preferred media types in the order of preference. The HW MFT then follows the sequence of events described in steps 4 through 9 of the previous section.

If the driver cannot handle such a format change, it should return a streaming error, which is then propagated to MF.

The following code example shows how to define a new dynamic format change by using a KSEVENT:

```
// {162AC456-83D7-4239-96DF-C75FFA138BC6}
#define STATIC_KSEVENTSETID_DynamicFormatChange\
    0x162ac456, 0x83d7, 0x4239, 0x96, 0xdf, 0xc7, 0x5f, 0xfa, 0x13, 0x8b, 0xc6 DEFINE_GUIDSTRUCT("162AC456-83D7-4239-96DF-C75FFA138BC6", KSEVENTSETID_ DynamicFormatChange);
#define KSEVENTSETID_DynamicFormatChange DEFINE_GUIDNAMED(KSEVENTSETID_ DynamicFormatChange)

typedef enum {
KSEVENT_DYNAMIC_FORMAT_CHANGE = 0
};

DEFINE_KSEVENT_TABLE(DynamicFormatChangeEventTable) {
    DEFINE_KSEVENT_ITEM
    (
        KSEVENT_DYNAMIC_FORMAT_CHANGE,
        sizeof(KSEVENTDATA),
        0,   
        NULL,
        NULL,
        NULL
    )
};

KSEVENT_SET PinEventTable[] =
{
    DEFINE_KSEVENT_SET
    (
        &KSEVENTSETID_DynamicFormatChange,
        SIZEOF_ARRAY(DynamicFormatChangeEventTable),
        DynamicFormatChangeEventTable
    )
};
```

Each pin should expose this event in its pin descriptor. The event is of type KSEVENTF\_EVENT\_HANDLE.

Before the driver generates this event, it should set the preferred media types for the KS pin based on the currently selected input media type. You can do this by using the [**\_KsEdit**](https://msdn.microsoft.com/library/windows/hardware/ff568796) function on the pin's descriptor.

To generate the event, drivers should call [**KsGenerateEvents**](https://msdn.microsoft.com/library/windows/hardware/ff562597).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Supporting%20Dynamic%20Format%20Changes%20in%20AVStream%20Codecs%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


