---
title: CCD Example Code
description: CCD Example Code
ms.assetid: 8ca2c7c4-8e6f-4e4f-9234-eb3e5dc164cc
keywords:
- connecting displays WDK Windows 7 display , CCD APIs, example code
- connecting displays WDK Windows Server 2008 R2 display , CCD APIs, example code
- configuring displays WDK Windows 7 display , CCD APIs, example code
- configuring displays WDK Windows Server 2008 R2 display , CCD APIs, example code
- CCD APIs WDK Windows 7 display , example code
- CCD APIs WDK Windows Server 2008 R2 display , example code
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# CCD Example Code


This section applies only to Windows 7 and later, and Windows Server 2008 R2 and later versions of Windows operating system.

The following C++ code shows several examples of how to get current display information, clone displays, and get device display information from the CCD API:

```c++
#include <iostream>
#include <vector>
#include <string>

#include <windows.h>

// Logs a std::string to the console
void log(const std::string& message) {
	if (message != "") {
		std::cout << message << std::endl;
	}
}

// Logs a std::wstring to the console
void log(const std::wstring& message) {
	if (message != L"") {
		std::wcout << message << std::endl;
	}
}

// Checks a LONG status code and returns true if the status
// is ERROR_SUCCESS. Prints the error and returns false 
// otherwise.
bool didSucceed(LONG status) {
	switch (status) {
	case ERROR_SUCCESS:
		return true;
	case ERROR_INVALID_PARAMETER: // 87L
		log("Invalid parameter");
		break;
	case ERROR_NOT_SUPPORTED: // 50L
		log("Not supported");
		break;
	case ERROR_ACCESS_DENIED: // 5L
		log("Access denied");
		std::cout << "Access denied" << std::endl;
		break;
	case ERROR_GEN_FAILURE: // 31L
		log("General failure");
		break;
	case ERROR_INSUFFICIENT_BUFFER: // 122L
		log("Insufficient buffer");
		break;
	}
	return false;
}

// Gets the main display, which has a source position of (0,0)
// Assumes that the passed in arrays were initialized via a successful
// QueryDisplayConfig call.
// Returns NULL if main display not found.
DISPLAYCONFIG_MODE_INFO* getPrimaryDisplay(DISPLAYCONFIG_MODE_INFO *modeInfoArr, UINT32 numModeInfoArrayElements) {
	for (unsigned int i = 0; i < numModeInfoArrayElements; i++) {
		DISPLAYCONFIG_MODE_INFO *item = &modeInfoArr[i];
		if (item->sourceMode.position.x == 0 && item->sourceMode.position.y == 0) {
			return item;
		}
	}
	return NULL;
}

// Extends displays without paying attention to the current 
// path or mode info
void extendDisplays() {
	SetDisplayConfig(0, NULL, 0, NULL, SDC_TOPOLOGY_EXTEND | SDC_APPLY);
}

// Clones displays without paying attention to the current 
// path or mode info
void cloneDisplays() {
	SetDisplayConfig(0, NULL, 0, NULL, SDC_TOPOLOGY_CLONE | SDC_APPLY);
}

// Attempts to clone the primary display to all other displays.
// Fails if primary display cannot be found at (0,0).
// Should only be called if topology == DISPLAYCONFIG_TOPOLOGY_CLONE.
bool alternateCloneDisplay(
	DISPLAYCONFIG_PATH_INFO *pathInfoArr, UINT32 numPathInfoArrayElements,
	DISPLAYCONFIG_MODE_INFO *modeInfoArr, UINT32 numModeInfoArrayElements) {
	DISPLAYCONFIG_MODE_INFO *primaryDisplay = getPrimaryDisplay(modeInfoArr, numModeInfoArrayElements);
	if (primaryDisplay != nullptr) {
		for (unsigned int i = 0; i < numPathInfoArrayElements; i++) {
			if (pathInfoArr[i].sourceInfo.id != primaryDisplay->id) {
				pathInfoArr[i].flags |= DISPLAYCONFIG_PATH_ACTIVE;
				pathInfoArr[i].sourceInfo.id = primaryDisplay->id;
				pathInfoArr[i].sourceInfo.modeInfoIdx = DISPLAYCONFIG_PATH_MODE_IDX_INVALID;
				pathInfoArr[i].targetInfo.modeInfoIdx = DISPLAYCONFIG_PATH_MODE_IDX_INVALID;
			}
		}
		return didSucceed(SetDisplayConfig(numPathInfoArrayElements, pathInfoArr, numModeInfoArrayElements, modeInfoArr, 
			SDC_APPLY | SDC_USE_SUPPLIED_DISPLAY_CONFIG | SDC_ALLOW_CHANGES | SDC_SAVE_TO_DATABASE));
	}
	return false;
}

// Returns the source device name for the given adapterId and id
std::wstring getSourceDeviceName(LUID adapterId, UINT32 id) {
	DISPLAYCONFIG_SOURCE_DEVICE_NAME deviceName;
	DISPLAYCONFIG_DEVICE_INFO_HEADER header;
	header.adapterId = adapterId;
	header.id = id;
	header.size = sizeof(DISPLAYCONFIG_SOURCE_DEVICE_NAME);
	header.type = DISPLAYCONFIG_DEVICE_INFO_GET_SOURCE_NAME;
	deviceName.header = header;
	LONG status = DisplayConfigGetDeviceInfo((DISPLAYCONFIG_DEVICE_INFO_HEADER*)&deviceName);
	if (didSucceed(status)) {
		return std::wstring(deviceName.viewGdiDeviceName);
	}
	return L"";
}

std::wstring getSourceDeviceName(DISPLAYCONFIG_PATH_INFO pathInfo) {
	return getSourceDeviceName(pathInfo.sourceInfo.adapterId, pathInfo.sourceInfo.id);
}

std::wstring getSourceDeviceName(DISPLAYCONFIG_MODE_INFO pathInfo) {
	return getSourceDeviceName(pathInfo.adapterId, pathInfo.id);
}

// Returns the monitor friendly device name.
// AdapterId and Id should both be from a target display, not a source.
// (e.g. DISPLAYCONFIG_PATH_INFO.targetInfo or 
//  DISPLAYCONFIG_MODE_INFO.infoType == DISPLAYCONFIG_MODE_INFO_TYPE_TARGET)
std::wstring getTargetFriendlyDeviceName(LUID adapterId, UINT32 id) {
	DISPLAYCONFIG_TARGET_DEVICE_NAME deviceName;
	DISPLAYCONFIG_DEVICE_INFO_HEADER header;
	header.adapterId = adapterId;
	header.id = id;
	header.size = sizeof(DISPLAYCONFIG_TARGET_DEVICE_NAME);
	header.type = DISPLAYCONFIG_DEVICE_INFO_GET_TARGET_NAME;
	deviceName.header = header;
	LONG status = DisplayConfigGetDeviceInfo((DISPLAYCONFIG_DEVICE_INFO_HEADER*)&deviceName);
	if (didSucceed(status)) {
		return std::wstring(deviceName.monitorFriendlyDeviceName);
	}
	return L"";
}

std::wstring getTargetFriendlyDeviceName(DISPLAYCONFIG_PATH_INFO pathInfo) {
	return getTargetFriendlyDeviceName(pathInfo.targetInfo.adapterId, pathInfo.targetInfo.id);
}

std::wstring getTargetFriendlyDeviceName(DISPLAYCONFIG_MODE_INFO pathInfo) {
	return getTargetFriendlyDeviceName(pathInfo.adapterId, pathInfo.id);
}

int __cdecl main(int argc, const char* argv[]) {
	// Get information on how many display configuration items there are
	UINT32 numPathArrayElements = 0;
	UINT32 numModeInfoArrayElements = 0;
	LONG status = GetDisplayConfigBufferSizes(QDC_DATABASE_CURRENT, &numPathArrayElements, &numModeInfoArrayElements);
	if (didSucceed(status)) {
		// Get all of the configuration information on each display
		DISPLAYCONFIG_PATH_INFO *pathInfoArr = new DISPLAYCONFIG_PATH_INFO[numPathArrayElements];
		DISPLAYCONFIG_MODE_INFO *modeInfoArr = new DISPLAYCONFIG_MODE_INFO[numModeInfoArrayElements];

		DISPLAYCONFIG_TOPOLOGY_ID currentTopology; // whether monitors are being extended, cloned, or used in some other fashion
		status = QueryDisplayConfig(QDC_DATABASE_CURRENT, &numPathArrayElements, pathInfoArr, &numModeInfoArrayElements, modeInfoArr, &currentTopology);
		if (didSucceed(status)) {
			log("Printing source device names from DISPLAYCONFIG_PATH_INFO");
			for (unsigned int i = 0; i < numPathArrayElements; i++) {
				log(L"PATH_INFO " + std::to_wstring(i+1) + L": " + getSourceDeviceName(pathInfoArr[i]));
				log(L"\t" + getTargetFriendlyDeviceName(pathInfoArr[i]));
			}
			log("------------");
			log("Printing source device names from DISPLAYCONFIG_MODE_INFO");
			for (unsigned int i = 0; i < numModeInfoArrayElements; i++) {
				if (modeInfoArr[i].infoType == DISPLAYCONFIG_MODE_INFO_TYPE_TARGET) {
					log(L"MODE_INFO " + std::to_wstring(i + 1) + L": " + getTargetFriendlyDeviceName(modeInfoArr[i]));
				}
			}
			log("------------");

			log("Looking for primary display...");
			DISPLAYCONFIG_MODE_INFO *primaryDisplay = getPrimaryDisplay(modeInfoArr, numModeInfoArrayElements);
			if (primaryDisplay != nullptr) {
				log("Found the primary display! It has an id of " + std::to_string(primaryDisplay->id) + 
					". Matching it up with a DISPLAYCONFIG_PATH_INFO with the same id...");
				if (currentTopology == DISPLAYCONFIG_TOPOLOGY_CLONE) {
					log("Looks like the current display is being cloned. You may get two+ results when matching...");
				}
				for (unsigned int i = 0; i < numPathArrayElements; i++) {
					DISPLAYCONFIG_PATH_INFO item = pathInfoArr[i];
					if (item.sourceInfo.id == primaryDisplay->id) {
						log(L"The primary display's source name is: " + getSourceDeviceName(pathInfoArr[i]));
						log(L"The nice name for this PATH_INFO item is: " + getTargetFriendlyDeviceName(pathInfoArr[i]));
					}
				}
			}
			else {
				log("Wasn't able to locate primary display at (0,0)");
			}
			log("Finished looking at primary vs other displays.");
			if (currentTopology != DISPLAYCONFIG_TOPOLOGY_CLONE && numPathArrayElements > 1) {
				log("Attempting to clone displays if we can...");
				bool result = alternateCloneDisplay(pathInfoArr, numPathArrayElements, modeInfoArr, numModeInfoArrayElements);
				if (result) {
					log("Successfully cloned displays");
				}
				else {
					log("Failed to clone displays");
				}
			}
		}
		delete[] pathInfoArr;
		delete[] modeInfoArr;
	}
}
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20CCD%20Example%20Code%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




