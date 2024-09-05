---
title: Use a QR code or URI link to download an eSIM profile
description: eSIM profiles downloads on Windows devices can be triggered by scanning a QR code or clicking on a URI
ms.date: 08/16/2024
author: mamoodyb
ms.author: mamoodyb
---

# Use a QR code or URI link to download an eSIM profile

Starting in Windows 11 23H2, Windows added functionality to recognize and properly handle URIs starting with the scheme name: ‘lpa:’. This enables Windows to scan eSIM QR codes from the Windows camera app or any third party app that can scan a QR code. This also enables mobile operators to embed ‘lpa:’ URIs into a webpage or email.

## What is an ‘lpa:’ URI?

This is a URI with the scheme name prefix ‘lpa:’. This prefix is defined for use with QR codes in GSMA eSIM spec SGP.22 section 4.1, but can be provided directly to a user embedded in a webpage button or email.  Windows will read this URI as follows: `lpa:[activation code]`

Windows will handle URIs with the ‘lpa:’ prefix from any application.

## What does the user see?
After the user clicks on an lpa URI, either from the camera app, browser, e-mail, or another app, Windows will launch the eSIM activation flow in the settings app under Network & Internet > Cellular > eSIM Profiles. This activation flow is the same as entering an activation code directly into the settings app.

## How should this be used?

Mobile operators are encouraged to incorporate lpa URIs to trigger eSIM profile downloads as part of their web buy flow. After completing a data plan purchase online, mobile operators can provide a link directly to the user to start a profile download either on a web page or through an e-mail.