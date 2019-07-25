---
title: Deprecation of Software Publisher Certificates and Commercial Release Certificates
description: Deprecation of Software Publisher Certificates and Commercial Release Certificates
ms.assetid: eafa4e20-94c5-49d6-a192-2fc7c9f1e64g
keywords:
- Trusted Root Certification Authorities certificate store WDK
- Trusted Publishers certificate store WDK

ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Reason for Deprecating Software Publisher Certificates and Commercial Release Certificates
lorem ipsum wee

# Frequently Asked Questions
## What alternatives to cross signed certificates are available for testing drivers?
As long as these drivers are timestamped before the expiration date of the intermediate, they will continue working.

## What will happen to my existing signed drivers? 
As long as these drivers are timestamped before the expiration date of the intermediate, they will continue working.

## Is there a way to run production drivers without exposing it to Microsoft? 
No, all production drivers must be submitted to, and signed by Microsoft. 

## Does every new version of my driver need to be resubmitted to hardware dev center?
Yes, every time a driver is rebuilt, it must be re-signed by Microsoft

## Will we continue to be able to sign code with our existing 3rd party issued certificates after 2021? 
Yes, these certificates will continue to work until they expire. Code signed by these certificates will only be able to run in user mode, and will not be allowed to run in the kernel, unless it has a valid Microsoft signature.

## Will I be able to continue using my EV certificate for signing submissions to Hardware Dev Center?  
Yes, EV certificates will continue to work until they expire. Only new kernel mode code signed by these EV certificates will no longer validate after the expiration. 

## How do I know if my signing certificate will be impacted by these expirations? 


## How can we automate Microsoft Test Signing to work with our build processes?
Hardware Dev Center provides an API that you can call through your build processes. Below is documentation, and some examples how to call into the API

[Hardware Dev Center API](/dashboard/api)

[GitHub Examples](https://github.com/Microsoft/SDCM)
## Starting in 2021, will Microsoft be the sole provider of production kernel mode code signatures? 