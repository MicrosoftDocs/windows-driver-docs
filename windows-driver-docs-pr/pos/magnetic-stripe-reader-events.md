---
title: Magnetic stripe reader events
description: Learn about the magnetic stripe reader events that are passed from the device driver to the Point of Service (POS) API layer by using ReadFile.
ms.date: 03/17/2023
---

# Magnetic stripe reader events

This section describes the events that are passed from the device driver to the Point of Service (POS) API layer by using [ReadFile](/windows/win32/api/fileapi/nf-fileapi-readfile). This section focuses on events that are specific to magnetic stripe readers (MSRs).

## In this section

[MagneticStripeReaderDataReceived](magneticstripereaderdatareceived.md)  
Occurs after a successful scan event.

[MagneticStripeReaderErrorOccured](magneticstripereadererroroccured.md)  
Occurs when there is an MSR error, such as a scanning error.
