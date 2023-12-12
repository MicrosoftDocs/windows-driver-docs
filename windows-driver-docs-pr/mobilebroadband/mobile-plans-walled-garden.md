---
title: Mobile Plans walled garden
description: Mobile Plans walled garden
keywords:
- Windows Mobile Plans mobile operators walled garden
ms.date: 12/12/2023
ms.topic: article
---

# Mobile Plans walled garden

The Mobile Plans *Walled Garden* is key to supporting customers when they run out of data. It enables them to reach the MO Direct portal even when there is no alternative internet connection such as Wi-Fi. This will enable consumers to purchase additional data plans and manage their subscriptions.

> [!NOTE]
> The Mobile Plans architecture does not support IP ranges for Walled Garden endpoints. Host names must be used for allowlisting.

The MO Direct web portal and `GetBalance` API endpoint must also be part of this Walled Garden.

## Walled Garden endpoints

There are only a small number of required endpoints that are always accessible to end users. The following table defines the endpoints required for Walled Garden.

| URL | HTTP/HTTPS |
| --- | --- |
| ctldl.windowsupdate.com | http |
| cdp1.public-trust.com | http |
| ocsp.omniroot.com | http |
| vassg142.ocsp.omniroot.com | http |
| vassg142.crl.omniroot.com | http |
| mscrl.microsoft.com | http |
| crl.microsoft.com | http |
| www.msftconnecttest.com | http |
| crl3.digicert.com | http |
| Ocsp.digicert.com | http |
| login.live.com | http + https |
| storagetos.datamart.windows.com | http + https |
| mps.datamart.windows.com | http + https |
| staging.datamart.windows.com | http + https |
| *smartscreen.microsoft.com | https |
