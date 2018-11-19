---
title: Bidirectional Communication Error Codes
description: The following error codes are used in printer bidirectional communication.
ms.assetid: e273f5eb-e4f4-4aa7-9ed9-b418eebc6144
keywords: ["graphics device interface (GDI),bidi error codes", "Windows graphics device interface (GDI),bidi error codes", "GDI,bidi error codes", "graphics device interface (GDI),bidirectional error codes", "Windows graphics device interface (GDI),bidirectional error codes", "GDI,bidirectional error codes", "graphics device interface (GDI),bidirectional error codes", "Windows graphics device interface (GDI),bidirectional error codes", "GDI,bidirectional error codes", "printing,bidi error codes", "printing,bidirectional error codes", "printing,bidirectional error codes", "bidi error codes", "bidirectional error codes", "bidirectional error codes"]
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# Bidirectional Communication Error Codes


The following error codes are used in printer bidirectional communication.

| Value                               | Description                                                                                            |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| ERROR\_BIDI\_DEVICE\_OFFLINE        | The bidi call is supported but the connection to the remote printer is not available.                  |
| ERROR\_BIDI\_ERROR\_BASE            | The bidi call completed successfully, but there are one or more errors in the individual responses.    |
| ERROR\_BIDI\_NOT\_SUPPORTED         | The bidi call is not supported by the port monitor or print provider.                                  |
| ERROR\_BIDI\_SCHEMA\_NOT\_SUPPORTED | A caller tried to access a bidi schema that is not supported by the port monitor or the print provider |
| ERROR\_BIDI\_SCHEMA\_READ\_ONLY     | A caller tried to set a read-only attribute.                                                           |
| ERROR\_BIDI\_SERVER\_OFFLINE        | The bidi call is supported but the connection to the remote printer server is not available.           |
| ERROR\_BIDI\_STATUS\_OK             | The bidi call completed successfully.                                                                  |
| ERROR\_BIDI\_STATUS\_WARNING        | The bidi call completed successfully, but there are one or more errors in the individual responses.    |
| ERROR\_NO\_DATA                     | The bidi schema is unknown.                                                                            |

 

 

 




