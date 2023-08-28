---
title: Deploying Audio Processing Objects
description: Instructions for deploying Audio Processing Object drivers to Windows 10 and Windows 11
ms.topic: article
ms.date: 08/28/2023
---

# Deploying Audio Processing Objects

The Windows audio engine supports third-party user-mode plugins for processing audio.
These are called "audio processing objects." The correct .inf class to use for drivers that install audio processing objects is different depending on the version of Windows.

## Deploying to Windows 11 and later

For Windows 11 21H2 (Sun Valley, build 22000) and later, all audio processing objects must be marked as `Class=AudioProcessingObject`. Shipping labels which deploy audio processing objects to Windows 11 21H2 and later with an incorrect .inf class are subject to rejection.

## Deploying to Windows 10

For Windows 10, all audio processing objects must be marked as `Class=SoftwareComponent`. Shipping labels which deploy audio processing objects to Windows 10 with an incorrect .inf class are subject to rejection.

Because users have the option to upgrade their Windows 10 machines to Windows 11, any shipping label that deploys an audio processing object to Windows 10 machines must have an OS ceiling to prevent it from being installed on Windows 11 machines. It must also have a corresponding shipping label for Windows 11 machines with an OS floor of Windows 11 21H2, which deploys a `Class=AudioProcessingObject` driver package to the same HWIDs and CHIDs.

## What to do if your shipping label is rejected

If your shipping label was rejected for one of the above reasons, please contact the Windows audio team at audio-partners@microsoft.com.