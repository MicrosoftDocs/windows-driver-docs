---
title: Barcode scanner events
description: Learn about the barcode scanner events that are passed from the device driver to the Point of Service (POS) API layer by using ReadFile.
ms.date: 03/17/2023
---

# Barcode scanner events

This section describes the events that are passed from the device driver to the Point of Service (POS) API layer by using [ReadFile](/windows/win32/api/fileapi/nf-fileapi-readfile). This section focuses on events that are specific to barcode scanners.

## In this section

[BarcodeScannerDataReceived](barcodescannerdatareceived.md)  
Occurs after a successful scan event.

[BarcodeScannerErrorOccurred](barcodescannererroroccurred.md)  
Occurs when there is an error, such as a scanning error.

[BarcodeScannerImagePreviewReceived](barcodescannerimagepreviewreceived.md)  
Occurs when the device receives a bitmap image of the scan.

[BarcodeScannerTriggerPressed](barcodescannertriggerpressed.md)  
Occurs when the barcode scanner trigger is pressed.

[BarcodeScannerTriggerReleased](barcodescannertriggerreleased.md)  
Occurs when the barcode scanner trigger is released.
