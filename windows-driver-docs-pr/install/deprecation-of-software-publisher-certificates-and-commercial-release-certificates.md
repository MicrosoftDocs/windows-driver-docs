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
The Microsoft Trusted Root Program has changed their policies to no longer give roots the ability to issue certificates with the ability to kernel mode code sign. You can view the policy here. Existing roots that had kernel mode code signing capabilities will continue working until they expire. However, the majority of these will expire in 2021. Below is a list of roots that will be expiring in 2021. 

|Common Name| Expiration date|
|-----------|---------------|
|VeriSign Class 3 Public Primary Certification Authority - G5		|2/22/2021|
|thawte Primary Root CA		                                        |2/22/2021|
|GeoTrust Primary Certification Authority		                    |2/22/2021|
|GeoTrust Primary Certification Authority - G3		                |2/22/2021|
|thawte Primary Root CA - G3		                                |2/22/2021|
|VeriSign Universal Root Certification Authority		            |2/22/2021|
|TC TrustCenter Class 2 CA II		                                |4/11/2021|
|COMODO RSA Certification Authority		                            |4/11/2021|
|UTN-USERFirst-Object		                                        |4/11/2021|
|DigiCert Assured ID Root CA		                                |4/15/2021|
|DigiCert High Assurance EV Root CA		                            |4/15/2021|
|DigiCert Global Root CA		                                    |4/15/2021|
|Entrust.net Certification Authority (2048)		                    |4/15/2021|
|GlobalSign Root CA		                                            |4/15/2021|
|Go Daddy Root Certificate Authority - G2		                    |4/15/2021|
|Starfield Root Certificate Authority - G2		                    |4/15/2021|
|NetLock Arany (Class Gold) Fotanúsítvány		                    |4/15/2021|
|NetLock Arany (Class Gold) Fotanúsítvány		                    |4/15/2021|
|NetLock Platina (Class Platinum) Fotanúsítvány		                |4/15/2021|
|Security Communication RootCA1		                                |4/15/2021|
|StartCom Certification Authority		                            |4/15/2021|
|Certum Trusted Network CA		                                    |4/15/2021|
|COMODO ECC Certification Authority		                            |4/11/2021|


# Frequently Asked Questions
#### What alternatives to cross signed certificates are available for testing drivers?
For all options below [TESTSIGNING boot option must be enabled](the-testsigning-boot-configuration-option.md)

#### What will happen to my existing signed drivers? 
As long as these drivers are timestamped before the expiration date of the intermediate, they will continue working.
- [MakeCert Process](makecert-test-certificate.md)
- [WHQL Test Signature Program](whql-test-signature-program.md)
- [Enterprise CA Process](enterprise-ca-test-certificate.md)

#### Is there a way to run production drivers without exposing it to Microsoft? 
No, all production drivers must be submitted to, and signed by Microsoft. 

#### Does every new version of my driver need to be resubmitted to hardware dev center?
Yes, every time a driver is rebuilt, it must be re-signed by Microsoft

#### Will we continue to be able to sign code with our existing 3rd party issued certificates after 2021? 
Yes, these certificates will continue to work until they expire. Code signed by these certificates will only be able to run in user mode, and will not be allowed to run in the kernel, unless it has a valid Microsoft signature.

#### Will I be able to continue using my EV certificate for signing submissions to Hardware Dev Center?  
Yes, EV certificates will continue to work until they expire. Only new kernel mode code signed by these EV certificates will no longer validate after the expiration. 

#### How do I know if my signing certificate will be impacted by these expirations? 


#### How can we automate Microsoft Test Signing to work with our build processes?
Hardware Dev Center provides an API that you can call through your build processes. Below is documentation, and some examples how to call into the API

[Hardware Dev Center API](/dashboard/dashboard-api.md)

[GitHub Examples](https://github.com/Microsoft/SDCM)

#### Starting in 2021, will Microsoft be the sole provider of production kernel mode code signatures? 
Yes

#### Hardware Dev Center doesn't provide driver signing for Windows XP, how can I have my drivers run in XP?
Drivers can still be signed with a 3rd party issued code signing certificate. However, the certificate that signed the driver will need to be installed in the machine’s “Trusted Publisher” folder. 
