---
title: XPS Driver Document Events
description: Provides information about XPS driver document events.
keywords:
- Version 3 XPS drivers WDK XPSDrv , events
- events WDK XPSDrv
- notifications WDK XPSDrv
- DrvDocumentEvent
ms.date: 01/31/2023
---

# XPS driver document events

[!include[Print Support Apps](../includes/print-support-apps.md)]

The Microsoft Windows Presentation Foundation (WPF) print support sends XPSDrv print drivers notification events during document spooling similarly to how GDI print support sends notifications to GDI print drivers. The WPF print support also uses the same **DrvDocumentEvent** DDI function that GDI print support uses, but new events have been defined to support XPS Document processing events. The GDI print support will continue to issue **DrvDocumentEvent** event handlers to GDI-based print drivers and XPSDrv print drivers for Microsoft Win32 application printing.

## DrvDocumentEvent event handler overview

If necessary, XPSDrv print drivers can export the **DrvDocumentEvent** event handler from the configuration module to intercept document processing functions. The new XPS Document-related events are identified by a symbolic name that starts with "DOCUMENTEVENT_XPS_".

The WPF print support calls the **DrvDocumentEvent** function of the XPSDrv print driver while it spools the document for printing. Each call occurs at a different step in the process. The processing step of each call is identified by the value of the *iEsc* argument. The contents of the buffers that are referenced by the *pvIn* and *pvOut* arguments vary, depending on the processing step.

The following subsections in this topic describes only the XPS Document processing events that the WPF print support produces.

## DrvDocumentEvent event handler description

The **DrvDocumentEvent** event handler has the following calling format. The code and parameter definitions in this section are only for information.

```cpp
INT
  DrvDocumentEvent(
    HANDLE  hPrinter,
    HDC  hdc,
    int  iEsc,
    ULONG  cbIn,
    PVOID  pvIn,
    ULONG  cbOut,
    PVOID  pvOut
    );
```

## Parameters

*hPrinter*  
The printer handle that the WPF print support provides.

*hdc*  
A caller-supplied device context handle that a [**CreateDC**](/windows/win32/api/wingdi/nf-wingdi-createdca) call generates. This parameter is zero if *iEsc* is set to DOCUMENTEVENT_CREATEDCPRE.

When a document is printed, the system will use the same event values for both XPS and GDI documents. The driver must be aware of this similarity and determine the type of the job based on the *hdc*. *hdc* is equal to INVALID_HANDLE_VALUE for all DOCUMENTEVENT_XPS_*Xxx* events. This check will determine the proper interpretation of the **DrvDocumentEvent** event values based on the calling application. This check is applicable to XPSDrv print drivers only.

*iEsc*  
A caller-supplied escape code that identifies the event to be handled. This parameter can be one of the following integer constants.

DOCUMENTEVENT_QUERYFILTER  
WPF print support sends this event to query the print driver for a list of XPS Document processing events to which the driver will respond. This event is issued before any other XPS Document-related events.

DOCUMENTEVENT_XPS_ADDFIXEDDOCUMENTSEQUENCEPRE  
WPF print support sends this event before it adds FixedDocumentSequence to the XPS spool file.

DOCUMENTEVENT_XPS_ADDFIXEDDOCUMENTSEQUENCEPOST  
WPF print support sends this event after it adds FixedDocumentSequence to the XPS spool file.

DOCUMENTEVENT_XPS_ADDFIXEDDOCUMENTPRE  
WPF print support sends this event before it adds FixedDocument to the XPS spool file.

DOCUMENTEVENT_XPS_ADDFIXEDDOCUMENTPOST  
WPF print support sends this event after it adds FixedDocument to the XPS spool file.

DOCUMENTEVENT_XPS_ADDFIXEDDOCUMENTSEQUENCEPRINTTICKETPRE  
WPF is about to add a PrintTicket to the FixedDocumentSequence (Job Level).

DOCUMENTEVENT_XPS_ADDFIXEDDOCUMENTSEQUENCEPRINTTICKETPOST  
WPF should free the data that the driver returns on the corresponding **DOCUMENTEVENT_XPS_ADDFIXEDDOCUMENTSEQUENCEPRINTTICKETPRE** event.

DOCUMENTEVENT_XPS_ADDFIXEDDOCUMENTPRINTTICKETPRE  
WPF is about to add a PrintTicket to the FixedDocument (Document Level).

DOCUMENTEVENT_XPS_ADDFIXEDDOCUMENTPRINTTICKETPOST  
WPF should free the data that the driver returns on the corresponding DOCUMENTEVENT_XPS_ADDFIXEDDOCUMENTPRINTTICKETPRE event.

DOCUMENTEVENT_XPS_ADDFIXEDPAGEPRINTTICKETPRE  
WPF is about to add a PrintTicket to the FixedPage (Page Level).

DOCUMENTEVENT_XPS_ADDFIXEDPAGEPRINTTICKETPOST  
WPF free the data that the driver returns on the corresponding DOCUMENTEVENT_XPS_ADDFIXEDPAGEPRINTTICKETPRE event.

DOCUMENTEVENT_XPS_CANCELJOB  
WPF print support sends this event before it calls a cancel job action.

DOCUMENTEVENT_XPS_COMMITJOB  
WPF finished writing the date to the current file.

*cbIn*  
The size, in bytes, of the buffer that the *pvln* parameter references. This value is provided by WPF print support and read by the event handler.

*pvIn*  
A caller-supplied pointer. The use of this parameter depends on the *iEsc* value, as the following list describes. (For the DOCUMENTEVENT_XPS_*Xxx* events that are not shown in this list, *pvIn* is not used.)

DOCUMENTEVENT_QUERYFILTER  
*pvIn* points to a PDOCEVENT_FILTER structure (the same as for DOCUMENTEVENT_QUERYFILTER).

DOCUMENTEVENT_XPS_ADDFIXEDDOCUMENTSEQUENCEPRE  
*pvIn* points to a PrintPropertiesCollection structure (see Winspool.h) that contains three properties:

- EscapeCode, which is EPrintPropertyType::kPropertyTypeInt32 (ULONG) value. The EscapeCode is the event value.

- JobIdentifier, which is a EPrintPropertyType::kPropertyTypeInt32 (ULONG) value. The JobIdentifier is the ID that is needed to call GetJob() and **SetJob**().

- JobName, which is a EPrintPropertyType:: kPropertyTypeString (UNICODE) value.

DOCUMENTEVENT_XPS_ADDFIXEDDOCUMENTSEQUENCEPOST  
The same as for DOCUMENTEVENT_XPS_ADDFIXEDDOCUMENTSEQUENCEPRE.

DOCUMENTEVENT_XPS_ADDFIXEDDOCUMENTPRE  
*pvIn* points to a PrintPropertiesCollection structure (see Winspool.h) that contains two properties:

- EscapeCode, which is a EPrintPropertyType::kPropertyTypeInt32 (ULONG) value. The EscapeCode is the event value.

- DocumentNumber, which is a EPrintPropertyType::kPropertyTypeInt32 (ULONG) value.

DOCUMENTEVENT_XPS_ADDFIXEDDOCUMENTPOST  
The same as for DOCUMENTEVENT_XPS_ADDFIXEDDOCUMENTPRE.

DOCUMENTEVENT_XPS_ADDFIXEDPAGEPRE  
*pvIn* points to a PrintPropertiesCollection structure (see Winspool.h) that contains two properties:

- EscapeCode, which is a EPrintPropertyType::kPropertyTypeInt32 (ULONG) value.

- PageNumber, which is a EPrintPropertyType::kPropertyTypeInt32 (ULONG) value.

DOCUMENTEVENT_XPS_ADDFIXEDPAGEPOST  
The same as for DOCUMENTEVENT_XPS_ADDFIXEDPAGEPRE.

DOCUMENTEVENT_XPS_ADDFIXEDDOCUMENTSEQUENCEPRINTTICKETPRE  
*pvIn* points to a PrintPropertiesCollection structure (see Winspool.h) that contains four properties:

- EscapeCode, which is a EPrintPropertyType::kPropertyTypeInt32 (ULONG). The EscapeCode is the event value.

- JobIdentifier, which is a EPrintPropertyType::kPropertyTypeInt32 (ULONG) value.

- JobName, which is a EPrintPropertyType:: kPropertyTypeString (UNICODE) value.

- PrintTicket, which is a EPrintPropertyType:: kPropertyTypeByte value.

You must allocate the PrintPropertiesCollection structure and its properties on the "PRE" event and free it on the corresponding "POST" event. You can set *pvOut* to **NULL** to indicate that you support the event but are not interested in changing the PrintTicket for a given document or page. The plug-in should never unload between "PRE" and "POST" events.

DOCUMENTEVENT_XPS_ADDFIXEDDOCUMENTSEQUENCEPRINTTICKETPOS  
*pvIn* is the same pointer as pvOut from DOCUMENTEVENT_XPS_ADDFIXEDDOCUMENTSEQUENCEPRINTTICKETPRE

The driver must free *pvIn*.

DOCUMENTEVENT_XPS_ADDFIXEDDOCUMENTPRINTTICKETPRE  
*pvIn* points to a PrintPropertiesCollection structure (see Winspool.h) that contains three properties:

- EscapeCode, which is a EPrintPropertyType::kPropertyTypeInt32 (ULONG) value. The EscapeCode is the event value.

- DocumentNumber, which is a EPrintPropertyType::kPropertyTypeInt32 (ULONG) value.

- PrintTicket, which is a EPrintPropertyType:: kPropertyTypeByte value.

You must allocate the PrintPropertiesCollection structure and its properties on the "PRE" event and free it on the corresponding "POST" event. You can set *pvOut* to **NULL** to indicate that you support the event but are not interested in changing the PrintTicket for a given document or page. The plug-in should never unload between "PRE" and "POST" events.

DOCUMENTEVENT_XPS_ADDFIXEDDOCUMENTPRINTTICKETPOS  
*pvIn* is the same pointer as *pvOut* from DOCUMENTEVENT_XPS_ADDFIXEDDOCUMENTPRINTTICKETPRE.

The driver must free *pvIn*.

DOCUMENTEVENT_XPS_ADDFIXEDPAGEPRINTTICKETPRE  
*pvIn* points to a PrintPropertiesCollection structure (see Winspool.h) that contains three properties:

- EscapeCode, which is a EPrintPropertyType::kPropertyTypeInt32 (ULONG) value. The EscapeCode is the event value.

- PageNumber, which is a EPrintPropertyType::kPropertyTypeInt32 (ULONG).

- PrintTicket, which is a EPrintPropertyType:: kPropertyTypeByte.

You must allocate the PrintPropertiesCollection structure and its properties on the "PRE" event and free it on the corresponding "POST" event. You can set *pvOut* to **NULL** to indicate that you support the event but are not interested in changing the PrintTicket for a given document or page. The plug-in should never unload between "PRE" and "POST" events.

>DOCUMENTEVENT_XPS_ADDFIXEDPAGEPRINTTICKETPOS  
*pvIn* is the same pointer as *pvOut* from DOCUMENTEVENT_XPS_ADDFIXEDPAGEPRINTTICKETPRE.

The driver must free *pvIn*.

DOCUMENTEVENT_XPS_CANCELJOB  
*pvIn* is **NULL**.

*cbOut*  
If the *iEsc* parameter contains **DOCUMENTEVENT_QUERYFILTER**, WPF print support provides the size of the buffer that the *pvOut* parameter references in the *cbOut* parameter. For all other values of *iEsc*, *cbOut* is not used.

pvOut  
The pointer to a buffer that the WPF print support provides. The buffer size and contents depend on the value of the *iEsc* parameter. The following list describes the contents of the *pvOut* buffer for each *iEsc* value.

DOCUMENTEVENT_QUERYFILTER  
A caller-supplied pointer to a buffer that contains a DOCEVENT_FILTER structure.

DOCUMENTEVENT_XPS_ADDFIXEDDOCUMENTSEQUENCEPRINTTICKETPRE  
A pointer to a PrintPropertiesCollection structure (see Winspool.h) that contains a "PrintTicket" property of type EPrintPropertyType::kPropertyTypeBuffer. This property is always present. When no PrintTicket is available, the value of PrintPropertyValue.propertyBlob.pBuf is **NULL**.

The property contains the XML PrintTicket, from which the Microsoft Windows Presentation Foundation (WPF) will use the PrintTicket instead of the one that the **XPSDocumentWriter** caller supplies. (If *pvOut* is **NULL** or the property is not present or the property data is **NULL**, WPF uses the caller-supplied PrintTicket.)

After this event is processed, WPF will call **DocumentEvent** with DOCUMENTEVENT_XPS_ADDFIXEDDOCUMENTSEQUENCEPRINTTICKETPOST for the driver to release *pvOut*.

DOCUMENTEVENT_XPS_ADDFIXEDDOCUMENTSEQUENCEPRINTTICKETPOS  
**NULL**

DOCUMENTEVENT_XPS_ADDFIXEDDOCUMENTPRINTTICKETPRE  
A pointer to a PrintPropertiesCollection structure (see Winspool.h) that contains a "PrintTicket" property of type EPrintPropertyType::PropertyTypeBuffer. This property is always present. When no PrintTicket is available, the value of **PrintPropertyValue**.propertyBlob.pBuf is **NULL**.

The property contains the XML PrintTicket, from which WPF will use the PrintTicket instead of the one that the **XPSDocumentWriter** caller supplies. (If *pvOut* is **NULL** or the property is not present or the property data is **NULL**, WPF uses the caller-supplied PrintTicket.)

After this event is processed, WPF will call **DocumentEvent** with DOCUMENTEVENT_XPS_ADDFIXEDDOCUMENTPRINTTICKETPOST for the driver to release *pvOut*.

DOCUMENTEVENT_XPS_ADDFIXEDDOCUMENTPRINTTICKETPOS  
**NULL**

DOCUMENTEVENT_XPS_ADDFIXEDPAGEPRINTTICKETPRE  
A pointer to a PrintPropertiesCollection structure (see Winspool.h) that contains a "PrintTicket" property of type EPrintPropertyType:: PropertyTypeBuffer. This property is always present. When no PrintTicket is available, the value of **PrintPropertyValue**.propertyBlob.pBuf is **NULL**.

The property contains the XML PrintTicket, from which WPF will use the PrintTicket instead of the one that the **XPSDocumentWriter** caller supplies. (If *pvOut* is **NULL** or the property is not present or the property data is **NULL**, WPF uses the caller-supplied PrintTicket.)

After this event is processed, WPF will call **DocumentEvent** with DOCUMENTEVENT_XPS_ADDFIXEDPAGEPRINTTICKETPOST for the driver to release *pvOut*.

DOCUMENTEVENT_XPS_ADDFIXEDPAGEPRINTTICKETPOS  
**NULL**

## Return value

**DrvDocumentEvent** returns one of the following values:

DOCUMENTEVENT_SUCCESS  
The driver successfully handled the escape code that *iEsc* identified.

DOCUMENTEVENT_FAILURE  
The driver supports the escape code that *iEsc* identified, but a failure occurred.

>DOCUMENTEVENT_UNSUPPORTED  
The driver does not support the escape code that *iEsc* identified.

## XPS document event structures and event code values

The following code example shows the structures and constants that the new XPS Document events use.

```cpp
//
// structures used in XPS Document events
//
 
typedef enum
    {
        kPropertyTypeString = 1,
        kPropertyTypeInt32,
        kPropertyTypeInt64,
        kPropertyTypeByte,
        kPropertyTypeTime,
        kPropertyTypeDevMode,
        kPropertyTypeSD,
        kPropertyTypeNotificationReply,
        kPropertyTypeNotificationOptions,

    } EPrintPropertyType;

    typedef struct
    {
        EPrintPropertyType       ePropertyType;
        union
        {
            BYTE                 propertyByte;
            PWSTR                propertyString;
            LONG                 propertyInt32;
            LONGLONG             propertyInt64;
            struct {
                DWORD  cbBuf;
                LPVOID pBuf;
            }                    propertyBlob;
        } value;

    }PrintPropertyValue;

    typedef struct
    {
        WCHAR*                  propertyName;
        PrintPropertyValue      propertyValue;

    }PrintNamedProperty;

    typedef struct
    {
        ULONG                   numberOfProperties;
        PrintNamedProperty*     propertiesCollection;

    }PrintPropertiesCollection;
```

The structures in the preceding code example are defined in Winspool.h.

The following escape codes are defined in Winddiui.h.

```cpp
//
 // Escape code for XPS Document events
//
#define DOCUMENTEVENT_QUERYFILTER                                     14
#define DOCUMENTEVENT_XPS_ADDFIXEDDOCUMENTSEQUENCEPRE                 1
// DOCUMENTEVENT_XPS_ADDFIXEDDOCUMENTSEQUENCEPRE must have same value as //DOCUMENTEVENT_CREATEDCPRE for Winspool.drv to query the driver for supported events and reset the cached events.
#define DOCUMENTEVENT_XPS_ADDFIXEDDOCUMENTPRE                         2
#define DOCUMENTEVENT_XPS_ADDFIXEDPAGEPRE        3                           
#define DOCUMENTEVENT_XPS_ADDFIXEDPAGEPOST                            4
#define DOCUMENTEVENT_XPS_ADDFIXEDDOCUMENTPOST                        5
#define DOCUMENTEVENT_XPS_ADDFIXEDDOCUMENTSEQUENCEPOST                13
// DOCUMENTEVENT_XPS_ADDFIXEDDOCUMENTSEQUENCEPOST must have same value as //DOCUMENTEVENT_STARTDOCPOST for Winspool.drv to signal the tray balloon that //the document is completed
#define DOCUMENTEVENT_XPS_CANCELJOB                                   6
#define DOCUMENTEVENT_XPS_ADDFIXEDDOCUMENTSEQUENCEPRINTTICKETPRE      7
#define DOCUMENTEVENT_XPS_ADDFIXEDDOCUMENTPRINTTICKETPRE              8
#define DOCUMENTEVENT_XPS_ADDFIXEDPAGEPRINTTICKETPRE                  9
#define DOCUMENTEVENT_XPS_ADDFIXEDPAGEPRINTTICKETPOST                 10
#define DOCUMENTEVENT_XPS_ADDFIXEDDOCUMENTPRINTTICKETPOST             11
#define DOCUMENTEVENT_XPS_ADDFIXEDDOCUMENTSEQUENCEPRINTTICKETPOST     12
```
