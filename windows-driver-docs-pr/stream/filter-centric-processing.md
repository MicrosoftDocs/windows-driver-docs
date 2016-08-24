---
title: Filter-Centric Processing
author: windows-driver-content
description: Filter-Centric Processing
MS-HAID:
- 'avsover\_a199fb72-2b5b-42fa-906a-b3e88381338d.xml'
- 'stream.filter\_centric\_processing'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: e56c5102-7ea6-4687-ae5e-1550db9500f0
keywords: ["filter-centric filters WDK AVStream", "AVStream filter-centric filters WDK", "filter types WDK AVStream", "AVStrMiniFilterProcess"]
---

# Filter-Centric Processing


## <a href="" id="ddk-filter-centric-processing-ksg"></a>


If a filter uses filter-centric processing, then by default AVStream calls the minidriver-supplied [*AVStrMiniFilterProcess*](https://msdn.microsoft.com/library/windows/hardware/ff556315) callback routine when there are data frames available on each pin instance. Minidrivers can modify this default behavior by setting the **Flags** member of the [**KSPIN\_DESCRIPTOR\_EX**](https://msdn.microsoft.com/library/windows/hardware/ff563534) structure.

To implement filter-centric processing, provide a pointer to a minidriver-supplied [*AVStrMiniFilterProcess*](https://msdn.microsoft.com/library/windows/hardware/ff556315) callback routine in the **Process** member of the [**KSFILTER\_DISPATCH**](https://msdn.microsoft.com/library/windows/hardware/ff562554) structure. Set the **Process** member of [**KSPIN\_DISPATCH**](https://msdn.microsoft.com/library/windows/hardware/ff563535) to **NULL**.

AVStream calls [*AVStrMiniFilterProcess*](https://msdn.microsoft.com/library/windows/hardware/ff556315) only when all of the following conditions are met:

-   Frames are available on pins that require frames for processing to occur. Minidrivers can modify processing behavior by setting flags in the **Flags** member of [**KSPIN\_DESCRIPTOR\_EX**](https://msdn.microsoft.com/library/windows/hardware/ff563534). Pay particular attention to combinations of the mutually exclusive flags KSPIN\_FLAG\_FRAMES\_NOT\_REQUIRED\_FOR\_PROCESSING and KSPIN\_FLAG\_SOME\_FRAMES\_REQUIRED\_FOR\_PROCESSING. The minidriver can also modify the set of pins that require frames through the use of the [**KsPinAttachAndGate**](https://msdn.microsoft.com/library/windows/hardware/ff563491) or [**KsPinAttachOrGate**](https://msdn.microsoft.com/library/windows/hardware/ff563492) routines.

-   The number of pin instances is equal to or greater than the **InstancesNecessary** member of the [**KSPIN\_DESCRIPTOR\_EX**](https://msdn.microsoft.com/library/windows/hardware/ff563534) structure. The **ClientState** member of the [**KSPIN**](https://msdn.microsoft.com/library/windows/hardware/ff563483) structure specifies the particular [**KSSTATE**](https://msdn.microsoft.com/library/windows/hardware/ff566856) enumerator at which the pin is currently set. After **InstancesNecessary** has been met, additional pins in the **KSSTATE\_STOP** state will not prevent filter processing.

-   The required number of pin instances is met (as specified by the **InstancesNecessary** member of the [**KSPIN\_DESCRIPTOR\_EX**](https://msdn.microsoft.com/library/windows/hardware/ff563534) structure.

-   The minidriver has not closed the process control gate of the filter by using the **KSGATE***Xxx* functions.

In the [*AVStrMiniFilterProcess*](https://msdn.microsoft.com/library/windows/hardware/ff556315) callback routine, the minidriver receives a pointer to an array of [**KSPROCESSPIN\_INDEXENTRY**](https://msdn.microsoft.com/library/windows/hardware/ff564260) structures. AVStream orders the array of KSPROCESSPIN\_INDEXENTRY structures by pin ID.

The following code examples illustrate how to use the process pin structures. The code is taken from the [AVStream Filter-Centric Simulated Capture Driver (Avssamp)](http://go.microsoft.com/fwlink/p/?linkid=256084) sample, which demonstrates how to write a filter-centric capture driver. Source code and a description of this sample are included in the MSDN Code Gallery.

The minidriver receives an array of KSPROCESSPIN\_INDEXENTRY structures in its filter process dispatch. In this example, the minidriver extracts the first KSPROCESSPIN structure from the KSPROCESSPIN\_INDEXENTRY structure of index VIDEO\_PIN\_ID:

```
NTSTATUS
CCaptureFilter::
Process (
    IN PKSPROCESSPIN_INDEXENTRY ProcessPinsIndex
    )
{
PKSPROCESSPIN VideoPin = NULL;
...
VideoPin = ProcessPinsIndex [VIDEO_PIN_ID].Pins [0];
...
}
```

The minidriver should not reference **ProcessPinsIndex** \[*n*\].**Pins** \[0\] before it has verified that the **Count** member of **ProcessPinsIndex** \[*n*\] is at least one, *or* that the **InstancesNecessary** member of the KSPIN\_DESCRIPTOR\_EX structure contained within **Pins** \[0\] is at least one. (If the latter is true, the pin is guaranteed to exist.)

Then, to specify the pin on which to capture frames, the [*AVStrMiniFilterProcess*](https://msdn.microsoft.com/library/windows/hardware/ff556315) callback routine passes a pointer to a KSPROCESSPIN structure to *CaptureFrame*, a vendor-supplied capture routine:

```
VidCapPin -> CaptureFrame (VideoPin, m_Tick);
```

The capture routine can then copy to or from the **Data** member of the KSPROCESSPIN structure. It might also update the **BytesUsed** and **Terminate** members of this structure, as in the following example:

```
RtlCopyMemory ( ProcessPin -> Data,
                m_SynthesisBuffer,
                m_VideoInfoHeader -> bmiHeader.biSizeImage
               );
ProcessPin -> BytesUsed = m_VideoInfoHeader -> bmiHeader.biSizeImage;
ProcessPin -> Terminate = TRUE;
```

The minidriver can also access the stream header structure corresponding to the current stream pointer and pin:

```
PKSSTREAM_HEADER StreamHeader = ProcessPin -> StreamPointer -> StreamHeader;
```

Most minidrivers that use filter-centric processing use the stream pointer only for stream header access. In the filter-centric model, AVStream manipulates the stream pointer internally. As a result, minidrivers should proceed with caution if they manipulate the stream pointer in a filter-centric driver.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Filter-Centric%20Processing%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


