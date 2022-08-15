---
title: ScannerStateReason element
description: The optional ScannerStateReason element specifies one piece of information about why the scanner is in its current state.
keywords: ["ScannerStateReason element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn ScannerStateReason
api_type:
- Schema
ms.date: 09/28/2021
---

# ScannerStateReason element

The optional **ScannerStateReason** element specifies one piece of information about why the scanner is in its current state.

## Usage

```xml
<wscn:ScannerStateReason>
  text
</wscn:ScannerStateReason>
```

## Attributes

There are no attributes.

## Text value

Required. One of the following values:

| Term | Description |
|--|--|
| AttentionRequired | The scan device requires user intervention before it can continue. |
| Calibrating | The scan device is calibrating its internal components to prepare to acquire images. |
| CoverOpen | One of more covers on the scan device are open. |
| InterlockOpen | The interlock is open. |
| InternalStorageFull | The internal storage component that is currently being written to is full. |
| LampError | The scanner lamp is failing and image acquisition cannot proceed. |
| LampWarming | The scanner lamp is warming to prepare to acquire images. |
| MediaJam | Media is jammed in one of the input sources, so image acquisition failed. |
| MultipleFeedError | The ADF was fed more than one piece of media simultaneously. |
| None | There are no current state reasons. |
| Paused | The scanner has paused, and the scanner state is Stopped. In this state, a scanner will not produce scanned output. |

## Child elements

There are no child elements.

## Parent elements

| Element |
|--|
| [**ScannerStateReasons**](scannerstatereasons.md) |

## Remarks

Some of these reasons describe scanner state that the scanner cannot enter according to the currently defined WSD Scan Service operation set. For example, the scanner can be **Paused** even though there is no "*PauseScanner*" operation. Such states are present because some other protocol or console action can cause the scanner to enter that state.

The WSD Scan Service must support the values that represent conditions that are detectable in its implementation. Therefore, a WSD Scan Service can support only that subset of allowed values that it can detect.

You can extend the allowed values, but there are implications when you extend this list on a client. The client typically localizes the [**ScannerStateReasons**](scannerstatereasons.md) value (as with other string variable values) to the language of the end user, so the client will not recognize a vendor extension value. However, the client can display the value that is received directly. This value should be in English, so some end users might not understand the value. Alternatively, the Scan Service can use the general **AttentionRequired** value and then explain the problem on the scanner console, which the user will see when they are at the scanner.

## See also

[**ScannerStateReasons**](scannerstatereasons.md)
