---
title: Filter-Centric Processing
description: Filter-Centric Processing
ms.assetid: e56c5102-7ea6-4687-ae5e-1550db9500f0
keywords:
- filter-centric filters WDK AVStream
- AVStream filter-centric filters WDK
- filter types WDK AVStream
- AVStrMiniFilterProcess
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Filter-Centric Processing





If a filter uses filter-centric processing, then by default AVStream calls the minidriver-supplied [*AVStrMiniFilterProcess*](https://msdn.microsoft.com/library/windows/hardware/ff556315) callback routine when there are data frames available on each pin instance. Minidrivers can modify this default behavior by setting the **Flags** member of the [**KSPIN\_DESCRIPTOR\_EX**](https://msdn.microsoft.com/library/windows/hardware/ff563534) structure.

To implement filter-centric processing, provide a pointer to a minidriver-supplied [*AVStrMiniFilterProcess*](https://msdn.microsoft.com/library/windows/hardware/ff556315) callback routine in the **Process** member of the [**KSFILTER\_DISPATCH**](https://msdn.microsoft.com/library/windows/hardware/ff562554) structure. Set the **Process** member of [**KSPIN\_DISPATCH**](https://msdn.microsoft.com/library/windows/hardware/ff563535) to **NULL**.

AVStream calls [*AVStrMiniFilterProcess*](https://msdn.microsoft.com/library/windows/hardware/ff556315) only when all of the following conditions are met:

-   Frames are available on pins that require frames for processing to occur. Minidrivers can modify processing behavior by setting flags in the **Flags** member of [**KSPIN\_DESCRIPTOR\_EX**](https://msdn.microsoft.com/library/windows/hardware/ff563534). Pay particular attention to combinations of the mutually exclusive flags KSPIN\_FLAG\_FRAMES\_NOT\_REQUIRED\_FOR\_PROCESSING and KSPIN\_FLAG\_SOME\_FRAMES\_REQUIRED\_FOR\_PROCESSING. The minidriver can also modify the set of pins that require frames through the use of the [**KsPinAttachAndGate**](https://msdn.microsoft.com/library/windows/hardware/ff563491) or [**KsPinAttachOrGate**](https://msdn.microsoft.com/library/windows/hardware/ff563492) routines.

-   The number of pin instances is equal to or greater than the **InstancesNecessary** member of the [**KSPIN\_DESCRIPTOR\_EX**](https://msdn.microsoft.com/library/windows/hardware/ff563534) structure. The **ClientState** member of the [**KSPIN**](https://msdn.microsoft.com/library/windows/hardware/ff563483) structure specifies the particular [**KSSTATE**](https://msdn.microsoft.com/library/windows/hardware/ff566856) enumerator at which the pin is currently set. After **InstancesNecessary** has been met, additional pins in the **KSSTATE\_STOP** state will not prevent filter processing.

-   The required number of pin instances is met (as specified by the **InstancesNecessary** member of the [**KSPIN\_DESCRIPTOR\_EX**](https://msdn.microsoft.com/library/windows/hardware/ff563534) structure.

-   The minidriver has not closed the process control gate of the filter by using the **KSGATE***Xxx* functions.

In the [*AVStrMiniFilterProcess*](https://msdn.microsoft.com/library/windows/hardware/ff556315) callback routine, the minidriver receives a pointer to an array of [**KSPROCESSPIN\_INDEXENTRY**](https://msdn.microsoft.com/library/windows/hardware/ff564260) structures. AVStream orders the array of KSPROCESSPIN\_INDEXENTRY structures by pin ID.

The following code examples illustrate how to use the process pin structures. The code is taken from the [AVStream Filter-Centric Simulated Capture Driver (Avssamp)](http://go.microsoft.com/fwlink/p/?linkid=256084) sample, which demonstrates how to write a filter-centric capture driver. Source code and a description of this sample are included in the Windows Driver Kit samples download.

The minidriver receives an array of KSPROCESSPIN\_INDEXENTRY structures in its filter process dispatch. In this example, the minidriver extracts the first KSPROCESSPIN structure from the KSPROCESSPIN\_INDEXENTRY structure of index VIDEO\_PIN\_ID:

```cpp
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

```cpp
VidCapPin -> CaptureFrame (VideoPin, m_Tick);
```

The capture routine can then copy to or from the **Data** member of the KSPROCESSPIN structure. It might also update the **BytesUsed** and **Terminate** members of this structure, as in the following example:

```cpp
RtlCopyMemory ( ProcessPin -> Data,
                m_SynthesisBuffer,
                m_VideoInfoHeader -> bmiHeader.biSizeImage
               );
ProcessPin -> BytesUsed = m_VideoInfoHeader -> bmiHeader.biSizeImage;
ProcessPin -> Terminate = TRUE;
```

The minidriver can also access the stream header structure corresponding to the current stream pointer and pin:

```cpp
PKSSTREAM_HEADER StreamHeader = ProcessPin -> StreamPointer -> StreamHeader;
```

Most minidrivers that use filter-centric processing use the stream pointer only for stream header access. In the filter-centric model, AVStream manipulates the stream pointer internally. As a result, minidrivers should proceed with caution if they manipulate the stream pointer in a filter-centric driver.
