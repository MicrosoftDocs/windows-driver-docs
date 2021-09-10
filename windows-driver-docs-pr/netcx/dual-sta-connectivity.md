# Dual STA connectivity

WiFiCx enables simultaneous connections to more than one STA (Secondary STA connectivity) when the client driver supports it. In its initial iteration this feature only supports a maximum of two STA connections, but this may change later.

## Configuring Secondary STA connectivity

The client driver indicates the ability to maintain Secondary STA connectivity during [adapter initialization](writing-a-wificx-client-driver.md) in the call to [**WifiDeviceSetStationCapabilities**](/windows-hardware/drivers/ddi/wificx/nf-wificx-wifidevicesetstationcapabilities). The driver must set the **NumSecondaryStaBandCombinations** and **SecondaryStaBandsCombinations** fields to non-zero values in the [**WIFI_STATION_CAPABILITIES**](/windows-hardware/drivers/ddi/wificx/ns-wificx-wifi_station_capabilities) structure. If those values are **0**/**NULL**, the Secondary STA capability will not be set.

## Current behavior

When the adapter supports Secondary STA connectivity there should be no full scan on the secondary STA since it's not visible to the user. Specific-purpose scans are an exception, such as when connecting over the secondary STA to discover connection candidates, or possibly for Neighbor reports. If the driver sees a scan request over the secondary STA, it should avoid scanning over the primary STA to minimize disruptions. The exception might be for co-located APs in the 6 GHz band, only if they can't be discovered on the other lower band scan.

When the driver supports Secondary STA connectivity, connections over the secondary STA are automatically synchronized with the primary STA. The initial connection over the secondary STA will start immediately after the primary STA connection succeeds, and will then follow a backoff timeout in case of failure.

## WiFiCx API TLV changes

Most of the API changes for enabling Secondary STA connectivity are documented here:

* [**WDI_TLV_CONNECT_PARAMETERS**](wdi-tlv-connect-parameters.md)
* [NDIS_STATUS_WDI_INDICATION_SECONDARY_STA_CONNECTIVITY](ndis-status-wdi-indication-secondary-sta-connectivity.md)
* [NDIS_STATUS_WDI_INDICATION_LINK_STATE_CHANGE](ndis-status-wdi-indication-link-state-change.md)

##	Secondary STA roam behavior

The driver should try to keep the secondary STA up while roaming on the primary STA band, even if it has to roam across bands. It should do this by synchronizing the roams so that both interfaces don’t end up roaming at the same time. The driver should keep the secondary STA up and wait for the roam to finish on the primary STA port (up to the point where the keys are plumbed for a secure connection) so that it can then select the appropriate roaming candidates for the secondary STA connection (on a different band than the primary STA). This will enable apps that are bound to both the primary and secondary STA interfaces to keep their connections up during the roam.
