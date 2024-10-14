---
title: Use a QR code or URI link to download an eSIM profile
description: eSIM profiles downloads on Windows devices can be triggered by scanning a QR code or clicking on a URI
ms.date: 08/16/2024
---

# Use a QR code or URI link to download an eSIM profile

Starting in Windows 11 24H2, functionality was added to recognize and properly handle URIs starting with the scheme name: *lpa:*. Supporting *lpa:* URIs enables Windows to scan eSIM QR codes from the Windows camera app or any non-Microsoft app that can scan QR codes. Mobile operators can also embed *lpa:* URIs into a webpage or email.

## What is a *lpa:* URI?

A *lpa:* URI is a Uniform Resource Identifier (URI) with the scheme name prefix *lpa:*. The *lpa:* prefix is defined for use with QR codes in GSMA eSIM spec SGP.22 section 4.1, but can be provided directly to a user embedded in a webpage button or email. Windows reads the URI as follows: `lpa:[activation code]`

Windows handles URIs with the *lpa:* prefix from any application.

## What does the user see?

After the user selects a *lpa:* URI from the camera app, browser, e-mail, or another app, Windows launches the eSIM activation flow in the settings app under **Network & Internet** > **Cellular** > **eSIM Profiles**. This activation flow is the same as entering an activation code directly into the **Settings** app.

## How should *lpa:* URIs be used?

Microsoft recommends that mobile operators incorporate *lpa:* URIs to trigger eSIM profile downloads as part of their web buy flow. After a customer completes a data plan purchase online, mobile operators can provide a link directly to the user to start a profile download either on a web page or through an e-mail.
