---
title: ACX audio data formats
description: This topic describes how ACX format types are used to help a driver to track, manage and compare signal data formats.  
ms.date: 03/15/2024
ms.localizationpriority: medium
ms.topic: concept-article
---

# ACX audio data formats and data format lists

This topic describes how ACX format types are used by a driver to track, manage and compare signal data formats. For a general overview of ACX, and a list of common ACX terms, see [ACX Audio Class Extensions Overview](acx-audio-class-extensions-overview.md). For general information on audio encoding formats, see [Audio Data Formats](audio-data-formats.md).

## ACXDATAFORMAT and ACXDATAFORMATLIST objects

Two ACX objects are used to work with data formats.

- ACXDATAFORMAT which represents a data format supported by the audio device.
- ACXDATAFORMATLIST which is a list of audio data formats available for use.

For more information about working with ACX objects, see [Summary of ACX Objects](acx-summary-of-objects.md).

ACX uses the [ACX_DATAFORMAT_TYPE enumeration](/windows-hardware/drivers/ddi/acxdataformat/ne-acxdataformat-acx_dataformat_type), which references a [KSDATAFORMAT structure](/windows-hardware/drivers/ddi/ks/ns-ks-ksdataformat) to specify a data format.

### ACXDATAFORMAT

ACXDATAFORMAT provides a handle to a data format object. Drivers create these objects using the [AcxDataFormatCreate](/windows-hardware/drivers/ddi/acxdataformat/nf-acxdataformat-acxdataformatcreate) function, and can compare them using [AcxDataFormatIsEqual](/windows-hardware/drivers/ddi/acxdataformat/nf-acxdataformat-acxdataformatisequal).

### ACXDATAFORMATLIST

ACXDATAFORMATLIST is a container for data format objects. When the driver creates an ACXPIN, ACX automatically creates an empty data format list for the raw signal processing mode. A driver can access the list using [AcxPinGetRawDataFormatList](/windows-hardware/drivers/ddi/acxpin/nf-acxpin-acxpingetrawdataformatlist). It returns the ACXDATAFORMATLIST for the specified ACXPIN.

A driver can add a format to a specific list using [AcxDataFormatListAddDataFormat](/windows-hardware/drivers/ddi/acxdataformat/nf-acxdataformat-acxdataformatlistadddataformat).

```cpp
    // The raw processing mode list is associated with each single circuit
    // by ACX. A driver uses AcxPinGetRawDataFormatList to retrieve the built-in raw
    // data-format list.
    //
    RETURN_NTSTATUS_IF_TRUE(CodecCaptureHostPin >= CodecCapturePinCount, STATUS_INVALID_PARAMETER);
    formatList = AcxPinGetRawDataFormatList(Pin[CodecCaptureHostPin]);
    RETURN_NTSTATUS_IF_TRUE(formatList == nullptr, STATUS_INSUFFICIENT_RESOURCES);

    //
    // The driver uses AcxDataFormatListAddDataFormat to add data formats to the raw
    // processing mode list associated with the current circuit.
    //
    RETURN_NTSTATUS_IF_FAILED(AcxDataFormatListAddDataFormat(formatList, formatPcm44100c1));
    RETURN_NTSTATUS_IF_FAILED(AcxDataFormatListAddDataFormat(formatList, formatPcm48000c1));
```

A driver can create additional data format lists and associated them to a specific signal processing mode using [AcxDataFormatListCreate](/windows-hardware/drivers/ddi/acxdataformat/nf-acxdataformat-acxdataformatlistcreate) for a specific WDFDEVICE such as ACXPIN.

`NTSTATUS AcxDataFormatListCreate(device, attributes, <format cfg>, &ACXDATAFORMATLIST)`

A driver can retrieve a format list associated with a specific pin using [AcxPinRetrieveModeDataFormatList](/windows-hardware/drivers/ddi/acxpin/nf-acxpin-acxpinretrievemodedataformatlist).

A driver can remove a format from a specific list using [AcxDataFormatListRemoveDataFormat](/windows-hardware/drivers/ddi/acxdataformat/nf-acxdataformat-acxdataformatlistremovedataformat). Note that if this format is also the default format, ACX selects the first one available in the list as default (if one is present).

A driver can specify a default format in the list using [AcxDataFormatListAssignDefaultDataFormat](/windows-hardware/drivers/ddi/acxdataformat/nf-acxdataformat-acxdataformatlistassigndefaultdataformat). The default format must be present in the list, else it will be added.

A driver can retrieve a default format in the list using [AcxDataFormatListRetrieveDefaultDataFormat](/windows-hardware/drivers/ddi/acxdataformat/nf-acxdataformat-acxdataformatlistretrievedefaultdataformat).

A driver can iterate over a format list and make changes as a group using the following DDIs.

- [AcxDataFormatListBeginIteration](/windows-hardware/drivers/ddi/acxdataformat/nf-acxdataformat-acxdataformatlistbeginiteration)
- [AcxDataFormatListRetrieveNextFormat](/windows-hardware/drivers/ddi/acxdataformat/nf-acxdataformat-acxdataformatlistretrievenextformat)
- [AcxDataFormatListEndIteration](/windows-hardware/drivers/ddi/acxdataformat/nf-acxdataformat-acxdataformatlistenditeration)

Note that the changes are applied only after the driver ends the iteration.

```cpp
VOID AcxDataFormatListBeginIteration(ACXDATAFORMATLIST, PACX_DATAFORMAT_LIST_ITERATOR)
NTSTATUS AcxDataFormatListRetrieveNextDataFormat(ACXDATAFORMATLIST,  PACX_DATAFORMAT_LIST_ITERATOR, &ACXFORMAT);
VOID AcxDataFormatListEndIteration(ACXDATAFORMATLIST, PACX_DATAFORMAT_LIST_ITERATOR)
```

The above DDIs remove the need for the driver to implement the following callbacks:

```cpp
PFN_ACX_PIN_GET_SIGNALPROCESSING_MODES      	EvtAcxPinGetSignalProcessingModes;
PFN_ACX_PIN_GET_DATAFORMATS                     EvtAcxPinGetDataFormats;
PFN_ACX_PIN_GET_DEFAULT_DATAFORMAT              EvtAcxPinGetDefaultDataFormat;
PFN_ACX_PIN_PROPOSE_DATAFORMAT                  EvtAcxPinProposeDataFormat;
```

The above DDIs also remove the need for the driver to implement the following events (ACX triggers this event automatically after the list has changed):

```cpp
// Clients enable this event to receive format change notifications. Drivers fire this even when it detects a dynamic format change on the specified pin (h/w pin).
//
    KSEVENT_PINCAPS_FORMATCHANGE(pin)
```

The above DDIs also remove the need for the driver to manage the modes and formats storage on its own.

The driver still needs to support the following DDI if the in/out formats are not the same (DSP circuit). This DDI is stream independent, circuit pin specific and only supported on non s/w streaming pins.

```cpp
PFN_ACX_PIN_SET_DATAFORMAT              EvtAcxPinSetDataFormat;
```

## See also

[acxdataformat.h header](/windows-hardware/drivers/ddi/acxdataformat/)

[Audio Data Formats](audio-data-formats.md)

[KSDATAFORMAT structure](/windows-hardware/drivers/ddi/ks/ns-ks-ksdataformat)

[ACX Audio Class Extensions overview](acx-audio-class-extensions-overview.md)
