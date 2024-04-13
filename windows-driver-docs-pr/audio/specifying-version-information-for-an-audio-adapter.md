---
title: Specifying Version Information for an Audio Adapter
description: Specifying Version Information for an Audio Adapter
keywords:
- audio adapters WDK , version information
- adapter drivers WDK audio , version information
- Port Class audio adapters WDK , version information
- versions WDK audio
ms.date: 04/20/2017
---

# Specifying Version Information for an Audio Adapter


## <span id="specifying_version_information_for_an_audio_adapter"></span><span id="SPECIFYING_VERSION_INFORMATION_FOR_AN_AUDIO_ADAPTER"></span>


A vendor should specify the following entries in the **Version** section of an INF file for a port-class audio adapter:

```inf
  Signature="$CHICAGO$"
  Class=MEDIA
  ClassGUID={4d36e96c-e325-11ce-bfc1-08002be10318}
```

For a description of additional version requirements and options for all device classes, see [**INF Version Section**](../install/inf-version-section.md).

 

