---
title: XpsAnalyzer Rules
description: XpsAnalyzer Rules
ms.assetid: 4f617665-4cc4-475d-ae66-abc2f00309fd
keywords:
- XpsAnalyzer WDK , rules
ms.date: 09/17/2018
ms.localizationpriority: medium
---

# XpsAnalyzer Rules

The following table describes the rules that the XpsAnalysis tool uses to analyze XPS files. These rules are based on the XML Paper Specification (XPS) 1.0 specification. For more information about this specification, doiwnload the [XML Paper Specification](http://download.microsoft.com/download/1/6/a/16acc601-1b7a-42ad-8d4e-4f0aa156ec3e/XPS_1_0.exe).

## Open Packaging Conventions (OPC) Rules

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Rule Name</th>
<th align="left">Data Type</th>
<th align="left">Explanation</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>CompressionOption</p></td>
<td align="left"><p>string</p></td>
<td align="left"><p>The value of the Compression option of the XPS package.</p></td>
</tr>
<tr class="even">
<td align="left"><p>CorruptedOpc</p></td>
<td align="left"><p>bool</p></td>
<td align="left"><p>True if the XPS package does not conform to the OPC specification.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>ForeignContentType</p></td>
<td align="left"><p>string</p></td>
<td align="left"><p>Content types that are not a part of the XPS specification.</p></td>
</tr>
<tr class="even">
<td align="left"><p>ForeignRelationshipType</p></td>
<td align="left"><p>string</p></td>
<td align="left"><p>Relationship types that are not a part of the XPS 1.0 specification.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>LargePartCount</p></td>
<td align="left"><p>long</p></td>
<td align="left"><p>The number of parts whose size exceeds a specified amount.</p></td>
</tr>
<tr class="even">
<td align="left"><p>MaxFileSizeInBytes</p></td>
<td align="left"><p>long</p></td>
<td align="left"><p>The maximum size of the set of parts within the XPS package.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>MaxPartRelationships</p></td>
<td align="left"><p>long</p></td>
<td align="left"><p>The maximum number of relationships for a part of the XPS package.</p></td>
</tr>
<tr class="even">
<td align="left"><p>PackageRelationshipCount</p></td>
<td align="left"><p>long</p></td>
<td align="left"><p>The total number of relationships in the XPS package.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>PartCount</p></td>
<td align="left"><p>long</p></td>
<td align="left"><p>The total number of parts in the OPC file.</p></td>
</tr>
<tr class="even">
<td align="left"><p>TotalPartRelationships</p></td>
<td align="left"><p>long</p></td>
<td align="left"><p>The total number of part relationships.</p></td>
</tr>
</tbody>
</table>

## XPS Trunk Rules

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Rule Name</th>
<th align="left">Data Type</th>
<th align="left">Explanation</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>CorruptedXpsTrunk</p></td>
<td align="left"><p>bool</p></td>
<td align="left"><p>True if the XPS package does not conform to the XPS 1.0 specification (Trunk level).</p></td>
</tr>
<tr class="even">
<td align="left"><p>FixedDocumentCount</p></td>
<td align="left"><p>long</p></td>
<td align="left"><p>The total number of documents in the XPS package.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>HasCoreProperties</p></td>
<td align="left"><p>bool</p></td>
<td align="left"><p>True if the XPS package contains the XPS Core Properties part.</p></td>
</tr>
<tr class="even">
<td align="left"><p>HasDiscardControl</p></td>
<td align="left"><p>bool</p></td>
<td align="left"><p>True if the XPS package contains the DiscardControl part.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>HasDocumentPrintTicket</p></td>
<td align="left"><p>bool</p></td>
<td align="left"><p>True if the XPS package contains the document-level PrintTicket.</p></td>
</tr>
<tr class="even">
<td align="left"><p>HasDocumentStructure</p></td>
<td align="left"><p>bool</p></td>
<td align="left"><p>True if the XPS package contains the DocumentStructure element.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>HasJobPrintTicket</p></td>
<td align="left"><p>bool</p></td>
<td align="left"><p>True if the XPS package contains the DocumentSequence-level PrintTicket.</p></td>
</tr>
<tr class="even">
<td align="left"><p>HasMoreThanOneSignatureBlockResourceInADocument</p></td>
<td align="left"><p>bool</p></td>
<td align="left"><p>True if the XPS package contains a document with more than one signature block resource.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>PackageThumbnailType</p></td>
<td align="left"><p>string</p></td>
<td align="left"><p>The image type of the XPS package-level thumbnail.</p></td>
</tr>
<tr class="even">
<td align="left"><p>SignatureBlockRequestCount</p></td>
<td align="left"><p>long</p></td>
<td align="left"><p>The total number of signatures in the XPS package.</p></td>
</tr>
</tbody>
</table>

 

## XPS Page Rules

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Rule Name</th>
<th align="left">Data Type</th>
<th align="left">Explanation</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>BleedBoxDimension</p></td>
<td align="left"><p>string</p></td>
<td align="left"><p>The dimension of NonDefault BleedBox in the XPS package.</p></td>
</tr>
<tr class="even">
<td align="left"><p>BrushCount</p></td>
<td align="left"><p>long</p></td>
<td align="left"><p>The total number of Brushes elements in the XPS package.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>CanvasCount</p></td>
<td align="left"><p>long</p></td>
<td align="left"><p>The total number of Canvas elements in the XPS package.</p></td>
</tr>
<tr class="even">
<td align="left"><p>CanvasLanguage</p></td>
<td align="left"><p>string</p></td>
<td align="left"><p>The language of the Canvas element.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>CanvasOpacityMaskBrush</p></td>
<td align="left"><p>string</p></td>
<td align="left"><p>The brush type of the Canvas OpacityMask element.</p></td>
</tr>
<tr class="even">
<td align="left"><p>ContentBoxDimension</p></td>
<td align="left"><p>string</p></td>
<td align="left"><p>The dimension of NonDefault ContentBox in the XPS package.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>CorruptedXpsPage</p></td>
<td align="left"><p>bool</p></td>
<td align="left"><p>True if the XPS package does not conform to the XPS 1.0 specification (Page level).</p></td>
</tr>
<tr class="even">
<td align="left"><p>FixedPageCount</p></td>
<td align="left"><p>long</p></td>
<td align="left"><p>The total number of Page elements in the XPS package.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>FontType</p></td>
<td align="left"><p>string</p></td>
<td align="left"><p>The font type found in the XPS package.</p></td>
</tr>
<tr class="even">
<td align="left"><p>GeometryCount</p></td>
<td align="left"><p>long</p></td>
<td align="left"><p>The total number of Geometry elements in the XPS package.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>GeometryFigureClosedFilledPatternRule</p></td>
<td align="left"><p>string</p></td>
<td align="left"><p>The type of the GeometryFigure.</p></td>
</tr>
<tr class="even">
<td align="left"><p>GeometryFigureMaxSegmentCount</p></td>
<td align="left"><p>long</p></td>
<td align="left"><p>The maximum number of SegmentCount elements in GeometryFigures.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>GeometryFigureMaxSegmentDataCount</p></td>
<td align="left"><p>long</p></td>
<td align="left"><p>The maximum number of SegmentDataCount elements in GeometryFigures.</p></td>
</tr>
<tr class="even">
<td align="left"><p>GeometryFigureSegmentStrokePattern</p></td>
<td align="left"><p>string</p></td>
<td align="left"><p>The stroke pattern of the GeometryFigures element.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>GeometryFigureSegmentType</p></td>
<td align="left"><p>string</p></td>
<td align="left"><p>The Segment Type of the GeometryFigure element.</p></td>
</tr>
<tr class="even">
<td align="left"><p>GeometryFillRule</p></td>
<td align="left"><p>string</p></td>
<td align="left"><p>The FillRule of the geometry.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>GlyphsBidiLevel</p></td>
<td align="left"><p>long</p></td>
<td align="left"><p>The BidiLevel of the Glyphs.</p></td>
</tr>
<tr class="even">
<td align="left"><p>GlyphsCount</p></td>
<td align="left"><p>long</p></td>
<td align="left"><p>The total number of Glyphs elements in the XPS package.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>GlyphsFillBrush</p></td>
<td align="left"><p>string</p></td>
<td align="left"><p>The brush type of the Glyphs Fill.</p></td>
</tr>
<tr class="even">
<td align="left"><p>GlyphsLanguage</p></td>
<td align="left"><p>string</p></td>
<td align="left"><p>The language of the Glyphs.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>GlyphsOpacityMaskBrush</p></td>
<td align="left"><p>string</p></td>
<td align="left"><p>The brush type of the Glyphs OpacityMask.</p></td>
</tr>
<tr class="even">
<td align="left"><p>GlyphsStyleSimulations</p></td>
<td align="left"><p>string</p></td>
<td align="left"><p>The StyleSimulations of the Glyphs.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>HasCanvasClipGeometryLocal</p></td>
<td align="left"><p>bool</p></td>
<td align="left"><p>True if the XPS package contains a Canvas element with local ClipGeometry.</p></td>
</tr>
<tr class="even">
<td align="left"><p>HasCanvasClipGeometryRemote</p></td>
<td align="left"><p>bool</p></td>
<td align="left"><p>True if the XPS package contains a Canvas element with remote ClipGeometry.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>HasCanvasHyperlinkTarget</p></td>
<td align="left"><p>bool</p></td>
<td align="left"><p>True if the XPS package contains a Canvas element with HyperlinkTarget.</p></td>
</tr>
<tr class="even">
<td align="left"><p>HasCanvasName</p></td>
<td align="left"><p>bool</p></td>
<td align="left"><p>True if the XPS package contains a Canvas element with Name property.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>HasCanvasOpacityEqualsOne</p></td>
<td align="left"><p>bool</p></td>
<td align="left"><p>True if the XPS package contains a Canvas element with Opacity=1.</p></td>
</tr>
<tr class="even">
<td align="left"><p>HasCanvasOpacityEqualsToZero</p></td>
<td align="left"><p>bool</p></td>
<td align="left"><p>True if the XPS package contains a Canvas element with Opacity=0.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>HasCanvasOpacityMaskBrushLocal</p></td>
<td align="left"><p>bool</p></td>
<td align="left"><p>True if the XPS package contains a Canvas element with local OpacityMaskBrush.</p></td>
</tr>
<tr class="even">
<td align="left"><p>HasCanvasOpacityMaskBrushRemote</p></td>
<td align="left"><p>bool</p></td>
<td align="left"><p>True if the XPS package contains a Canvas element with remote OpacityMaskBrush.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>HasCanvasTransformLocal</p></td>
<td align="left"><p>bool</p></td>
<td align="left"><p>True if the XPS package contains a Canvas element with local MatrixTransform.</p></td>
</tr>
<tr class="even">
<td align="left"><p>HasCanvasTransformRemote</p></td>
<td align="left"><p>bool</p></td>
<td align="left"><p>True if the XPS package contains a Canvas element with remote MatrixTransform.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>HasCanvasWithAccessibilityLongDescription</p></td>
<td align="left"><p>bool</p></td>
<td align="left"><p>True if the XPS package contains a Canvas element with AccessibilityLongDescription.</p></td>
</tr>
<tr class="even">
<td align="left"><p>HasCanvasWithAccessibilityShortDescription</p></td>
<td align="left"><p>bool</p></td>
<td align="left"><p>True if the XPS package contains a Canvas element with AccessibilityShortDescription.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>HasCanvasWithUseAliasedEdgeMode</p></td>
<td align="left"><p>bool</p></td>
<td align="left"><p>True if the XPS package contains a Canvas element with UseAliasedEdgeMode=True.</p></td>
</tr>
<tr class="even">
<td align="left"><p>HasColorProfile</p></td>
<td align="left"><p>bool</p></td>
<td align="left"><p>True if the XPS package contains ColorProfile.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>HasGeometryFigureWithMultipleSegmentTypes</p></td>
<td align="left"><p>bool</p></td>
<td align="left"><p>True if the XPS package contains a GeometryFigure element with multiple segment types.</p></td>
</tr>
<tr class="even">
<td align="left"><p>HasGeometryFigureWithNonDefaultStartPoint</p></td>
<td align="left"><p>bool</p></td>
<td align="left"><p>True if the XPS package contains a GeometryFigure element with non default StartPoint (0.0, 0.0).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>HasGeometryTransformLocal</p></td>
<td align="left"><p>bool</p></td>
<td align="left"><p>True if the XPS package contains a geometry with local MatrixTransform.</p></td>
</tr>
<tr class="even">
<td align="left"><p>HasGeometryTransformRemote</p></td>
<td align="left"><p>bool</p></td>
<td align="left"><p>True if the XPS package contains a geometry with remote MatrixTransform.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>HasGlyphsClipGeometryLocal</p></td>
<td align="left"><p>bool</p></td>
<td align="left"><p>True if the XPS package contains a Glyphs with local ClipGeometry.</p></td>
</tr>
<tr class="even">
<td align="left"><p>HasGlyphsClipGeometryRemote</p></td>
<td align="left"><p>bool</p></td>
<td align="left"><p>True if the XPS package contains a Glyphs element with remote ClipGeometry.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>HasGlyphsDeviceFontName</p></td>
<td align="left"><p>bool</p></td>
<td align="left"><p>True if the XPS package contains a Glyphs element with DeviceFontName.</p></td>
</tr>
<tr class="even">
<td align="left"><p>HasGlyphsFillBrushLocal</p></td>
<td align="left"><p>bool</p></td>
<td align="left"><p>True if the XPS package contains a Glyphs element with local FillBrush.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>HasGlyphsFillBrushRemote</p></td>
<td align="left"><p>bool</p></td>
<td align="left"><p>True if the XPS package contains a Glyphs element with remote FillBrush.</p></td>
</tr>
<tr class="even">
<td align="left"><p>HasGlyphsFontFaceIndex</p></td>
<td align="left"><p>bool</p></td>
<td align="left"><p>True if the XPS package contains a Glyphs element with FontFaceIndex.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>HasGlyphsHyperlinkTarget</p></td>
<td align="left"><p>bool</p></td>
<td align="left"><p>True if the XPS package contains a Glyphs element with HyperlinkTarget.</p></td>
</tr>
<tr class="even">
<td align="left"><p>HasGlyphsName</p></td>
<td align="left"><p>bool</p></td>
<td align="left"><p>True if the XPS package contains a Glyphs element with Name property.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>HasGlyphsOpacityEqualsOne</p></td>
<td align="left"><p>bool</p></td>
<td align="left"><p>True if the XPS package contains a Glyphs element with Opacity=1.</p></td>
</tr>
<tr class="even">
<td align="left"><p>HasGlyphsOpacityEqualsToZero</p></td>
<td align="left"><p>bool</p></td>
<td align="left"><p>True if the XPS package contains a Glyphs element with Opacity=0.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>HasGlyphsOpacityMaskBrushLocal</p></td>
<td align="left"><p>bool</p></td>
<td align="left"><p>True if the XPS package contains a Glyphs element with local OpacityMaskBrush.</p></td>
</tr>
<tr class="even">
<td align="left"><p>HasGlyphsOpacityMaskBrushRemote</p></td>
<td align="left"><p>bool</p></td>
<td align="left"><p>True if the XPS package contains a Glyphs element with remote OpacityMaskBrush.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>HasGlyphsTransformLocal</p></td>
<td align="left"><p>bool</p></td>
<td align="left"><p>True if the XPS package contains a Glyphs element with local MatrixTransform.</p></td>
</tr>
<tr class="even">
<td align="left"><p>HasGlyphsTransformRemote</p></td>
<td align="left"><p>bool</p></td>
<td align="left"><p>True if the XPS package contains a Glyphs element with remote MatrixTransform.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>HasGlyphsUnicodeString</p></td>
<td align="left"><p>bool</p></td>
<td align="left"><p>True if the XPS package contains a Glyphs element with UnicodeString.</p></td>
</tr>
<tr class="even">
<td align="left"><p>HasGlyphsWithSideways</p></td>
<td align="left"><p>bool</p></td>
<td align="left"><p>True if the XPS package contains a Glyphs element with IsSideways property enabled.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>HasHyperlinkTarget</p></td>
<td align="left"><p>bool</p></td>
<td align="left"><p>True if the XPS package contains a page with aHyperlink target.</p></td>
</tr>
<tr class="even">
<td align="left"><p>HasImageBrushOpacityEqualsToOne</p></td>
<td align="left"><p>bool</p></td>
<td align="left"><p>True if the XPS package contains an ImageBrush with Opacity=1.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>HasImageBrushOpacityEqualsToZero</p></td>
<td align="left"><p>bool</p></td>
<td align="left"><p>True if the XPS package contains an ImageBrush with Opacity=0.</p></td>
</tr>
<tr class="even">
<td align="left"><p>HasImageBrushTransformLocal</p></td>
<td align="left"><p>bool</p></td>
<td align="left"><p>True if the XPS package contains an ImageBrush with Local MatrixTransform.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>HasImageBrushTransformRemote</p></td>
<td align="left"><p>bool</p></td>
<td align="left"><p>True if the XPS package contains an ImageBrush with Remote MatrixTransform.</p></td>
</tr>
<tr class="even">
<td align="left"><p>HasImageBrushWithColorProfileResource</p></td>
<td align="left"><p>bool</p></td>
<td align="left"><p>True if the XPS package contains an ImageBrush with ColorProfileResource.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>HasImageBrushWithNonDefaultViewBox</p></td>
<td align="left"><p>bool</p></td>
<td align="left"><p>True if the XPS package contains an ImageBrush with a NonDefault ViewBox (0, 0, 1, 1).</p></td>
</tr>
<tr class="even">
<td align="left"><p>HasImageBrushWithNonDefaultViewPort</p></td>
<td align="left"><p>bool</p></td>
<td align="left"><p>True if the XPS package contains an ImageBrush with a NonDefault ViewPort (0, 0, 1, 1).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>HasLinearGradientBrushOpacityEqualsToOne</p></td>
<td align="left"><p>bool</p></td>
<td align="left"><p>True if the XPS package contains a LinearGradientBrush with Opacity=1.</p></td>
</tr>
<tr class="even">
<td align="left"><p>HasLinearGradientBrushOpacityEqualsToZero</p></td>
<td align="left"><p>bool</p></td>
<td align="left"><p>True if the XPS package contains a LinearGradientBrush with Opacity=0.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>HasLinearGradientBrushTransformLocal</p></td>
<td align="left"><p>bool</p></td>
<td align="left"><p>True if the XPS package contains a LinearGradientBrush with Local MatrixTransform.</p></td>
</tr>
<tr class="even">
<td align="left"><p>HasLinearGradientBrushTransformRemote</p></td>
<td align="left"><p>bool</p></td>
<td align="left"><p>True if the XPS package contains a LinearGradientBrush with Remote MatrixTransform.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>HasLinearGradientBrushWithColorProfileResource</p></td>
<td align="left"><p>bool</p></td>
<td align="left"><p>True if the XPS package contains a LinearGradientBrush with ColorProfileResource.</p></td>
</tr>
<tr class="even">
<td align="left"><p>HasLinearGradientBrushWithNonDefaultEndPoint</p></td>
<td align="left"><p>string</p></td>
<td align="left"><p>True if the XPS package contains a LinearGradientBrush with a NonDefault EndPoint.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>HasLinearGradientBrushWithNonDefaultGradientStopOffset</p></td>
<td align="left"><p>bool</p></td>
<td align="left"><p>True if the XPS package contains a LinearGradientBrush with a NonDefault GradientStopOffset.</p></td>
</tr>
<tr class="even">
<td align="left"><p>HasLinearGradientBrushWithNonDefaultStartPoint</p></td>
<td align="left"><p>string</p></td>
<td align="left"><p>True if the XPS package contains a LinearGradientBrush with a NonDefault StartPoint.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>HasLocalDictionary</p></td>
<td align="left"><p>bool</p></td>
<td align="left"><p>True if the XPS package contains a page that uses a Local Dictionary.</p></td>
</tr>
<tr class="even">
<td align="left"><p>HasNonDefaultBleedBox</p></td>
<td align="left"><p>bool</p></td>
<td align="left"><p>True if the XPS package contains a page with a NonDefault BleedBox value.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>HasNonDefaultContentBox</p></td>
<td align="left"><p>bool</p></td>
<td align="left"><p>True if the XPS package contains a page with a NonDefault ContentBox value.</p></td>
</tr>
<tr class="even">
<td align="left"><p>HasPageName</p></td>
<td align="left"><p>bool</p></td>
<td align="left"><p>True if the XPS package contains a page with the Name attribute set.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>HasPagePrintTicket</p></td>
<td align="left"><p>bool</p></td>
<td align="left"><p>True if the XPS package contains a Page level PrintTicket.</p></td>
</tr>
<tr class="even">
<td align="left"><p>HasPathClipGeometryLocal</p></td>
<td align="left"><p>bool</p></td>
<td align="left"><p>True if the XPS package contains a Path with local ClipGeometry</p></td>
</tr>
<tr class="odd">
<td align="left"><p>HasPathClipGeometryRemote</p></td>
<td align="left"><p>bool</p></td>
<td align="left"><p>True if the XPS package contains a Path with a remote ClipGeometry value.</p></td>
</tr>
<tr class="even">
<td align="left"><p>HasPathFillBrushLocal</p></td>
<td align="left"><p>bool</p></td>
<td align="left"><p>True if the XPS package contains a Path with local FillBrush.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>HasPathFillBrushRemote</p></td>
<td align="left"><p>bool</p></td>
<td align="left"><p>True if the XPS package contains a Path with remote FillBrush.</p></td>
</tr>
<tr class="even">
<td align="left"><p>HasPathGeometryLocal</p></td>
<td align="left"><p>bool</p></td>
<td align="left"><p>True if the XPS package contains a Path with local a Geometry property.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>HasPathGeometryRemote</p></td>
<td align="left"><p>bool</p></td>
<td align="left"><p>True if the XPS package contains a Path with a remote Geometry property.</p></td>
</tr>
<tr class="even">
<td align="left"><p>HasPathHyperlinkTarget</p></td>
<td align="left"><p>bool</p></td>
<td align="left"><p>True if the XPS package contains a Path with a HyperlinkTarget value.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>HasPathName</p></td>
<td align="left"><p>bool</p></td>
<td align="left"><p>True if the XPS package contains a Path with a Name property.</p></td>
</tr>
<tr class="even">
<td align="left"><p>HasPathOpacityEqualsOne</p></td>
<td align="left"><p>bool</p></td>
<td align="left"><p>True if the XPS package contains a Path with Opacity=1.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>HasPathOpacityEqualsToZero</p></td>
<td align="left"><p>bool</p></td>
<td align="left"><p>True if the XPS package contains a Path with Opacity=0.</p></td>
</tr>
<tr class="even">
<td align="left"><p>HasPathOpacityMaskBrushLocal</p></td>
<td align="left"><p>bool</p></td>
<td align="left"><p>True if the XPS package contains a Path with a local OpacityMaskBrush value.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>HasPathOpacityMaskBrushRemote</p></td>
<td align="left"><p>bool</p></td>
<td align="left"><p>True if the XPS package contains a Path with remote an OpacityMaskBrush.</p></td>
</tr>
<tr class="even">
<td align="left"><p>HasPathStrokeBrushLocal</p></td>
<td align="left"><p>bool</p></td>
<td align="left"><p>True if the XPS package contains a Path with a local StrokeBrush property.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>HasPathStrokeBrushRemote</p></td>
<td align="left"><p>bool</p></td>
<td align="left"><p>True if the XPS package contains a Path with a remote StrokeBrush property.</p></td>
</tr>
<tr class="even">
<td align="left"><p>HasPathStrokeDashOffset</p></td>
<td align="left"><p>bool</p></td>
<td align="left"><p>True if the XPS package contains a Path with StrokeDashOffset.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>HasPathTransformLocal</p></td>
<td align="left"><p>bool</p></td>
<td align="left"><p>True if the XPS package contains a Path with a local MatrixTransform.</p></td>
</tr>
<tr class="even">
<td align="left"><p>HasPathTransformRemote</p></td>
<td align="left"><p>bool</p></td>
<td align="left"><p>True if the XPS package contains a Path with a remote MatrixTransform.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>HasPathWithAccessibilityLongDescription</p></td>
<td align="left"><p>bool</p></td>
<td align="left"><p>True if the XPS package contains a Path with AccessibilityLongDescription value.</p></td>
</tr>
<tr class="even">
<td align="left"><p>HasPathWithAccessibilityShortDescription</p></td>
<td align="left"><p>bool</p></td>
<td align="left"><p>True if the XPS package contains a Path with AccessibilityShortDescription</p></td>
</tr>
<tr class="odd">
<td align="left"><p>HasPathWithNonDefaultStrokeMiterLimit</p></td>
<td align="left"><p>bool</p></td>
<td align="left"><p>True if the XPS package contains a Path with a NonDefault StrokeMiterLimit.</p></td>
</tr>
<tr class="even">
<td align="left"><p>HasPathWithNonDefaultStrokeThickness</p></td>
<td align="left"><p>bool</p></td>
<td align="left"><p>True if the XPS package contains a Path with a NonDefault StrokeThickness.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>HasPathWithSnapsToPixel</p></td>
<td align="left"><p>bool</p></td>
<td align="left"><p>True if the XPS package contains a Path with a SnapToPixels value.</p></td>
</tr>
<tr class="even">
<td align="left"><p>HasRadialGradientBrushOpacityEqualsToOne</p></td>
<td align="left"><p>bool</p></td>
<td align="left"><p>True if the XPS package contains a RadialGradientBrush with Opacity=1.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>HasRadialGradientBrushOpacityEqualsToZero</p></td>
<td align="left"><p>bool</p></td>
<td align="left"><p>True if the XPS package contains a RadialGradientBrush with Opacity=0.</p></td>
</tr>
<tr class="even">
<td align="left"><p>HasRadialGradientBrushTransformLocal</p></td>
<td align="left"><p>bool</p></td>
<td align="left"><p>True if the XPS package contains a RadialGradientBrush with Local MatrixTransform.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>HasRadialGradientBrushTransformRemote</p></td>
<td align="left"><p>bool</p></td>
<td align="left"><p>True if the XPS package contains a RadialGradientBrush with Remote MatrixTransform.</p></td>
</tr>
<tr class="even">
<td align="left"><p>HasRadialGradientBrushWithColorProfileResource</p></td>
<td align="left"><p>bool</p></td>
<td align="left"><p>True if the XPS package contains a RadialGradientBrush with ColorProfileResource.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>HasRadialGradientBrushWithNonDefaultCenter</p></td>
<td align="left"><p>bool</p></td>
<td align="left"><p>True if the XPS package contains a RadialGradientBrush with a NonDefault Center.</p></td>
</tr>
<tr class="even">
<td align="left"><p>HasRadialGradientBrushWithNonDefaultGradientOrigin</p></td>
<td align="left"><p>bool</p></td>
<td align="left"><p>True if the XPS package contains a RadialGradientBrush with a NonDefault GradientOrigin.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>HasRadialGradientBrushWithNonDefaultGradientStopOffset</p></td>
<td align="left"><p>bool</p></td>
<td align="left"><p>True if the XPS package contains a RadialGradientBrush with a NonDefault GradientStopOffset.</p></td>
</tr>
<tr class="even">
<td align="left"><p>HasRadialGradientBrushWithNonDefaultRadiiSizes</p></td>
<td align="left"><p>bool</p></td>
<td align="left"><p>True if the XPS package contains a RadialGradientBrush with a NonDefault RadiiSizes.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>HasRemoteDictionary</p></td>
<td align="left"><p>bool</p></td>
<td align="left"><p>True if the XPS package contains a page that uses a RemoteDictionary.</p></td>
</tr>
<tr class="even">
<td align="left"><p>HasSolidColorBrushOpacityEqualsToOne</p></td>
<td align="left"><p>bool</p></td>
<td align="left"><p>True if the XPS package contains a SolidColorBrush with Opacity=1.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>HasSolidColorBrushOpacityEqualsToZero</p></td>
<td align="left"><p>bool</p></td>
<td align="left"><p>True if the XPS package contains a SolidColorBrush with Opacity=0.</p></td>
</tr>
<tr class="even">
<td align="left"><p>HasSolidColorBrushWithColorProfileResource</p></td>
<td align="left"><p>bool</p></td>
<td align="left"><p>True if the XPS package contains a SolidColorBrush with ColorProfileResource.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>HasStoryFragment</p></td>
<td align="left"><p>bool</p></td>
<td align="left"><p>True if the XPS package contains a StoryFragment part.</p></td>
</tr>
<tr class="even">
<td align="left"><p>HasVisualBrushOpacityEqualsToOne</p></td>
<td align="left"><p>bool</p></td>
<td align="left"><p>True if the XPS package contains a VisualBrush element with Opacity=1.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>HasVisualBrushOpacityEqualsToZero</p></td>
<td align="left"><p>bool</p></td>
<td align="left"><p>True if the XPS package contains a VisualBrush element with Opacity=0.</p></td>
</tr>
<tr class="even">
<td align="left"><p>HasVisualBrushTransformLocal</p></td>
<td align="left"><p>bool</p></td>
<td align="left"><p>True if the XPS package contains a VisualBrush element with Local MatrixTransform.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>HasVisualBrushTransformRemote</p></td>
<td align="left"><p>bool</p></td>
<td align="left"><p>True if the XPS package contains a VisualBrush element with Remote MatrixTransform.</p></td>
</tr>
<tr class="even">
<td align="left"><p>HasVisualBrushWithLocalCanvas</p></td>
<td align="left"><p>bool</p></td>
<td align="left"><p>True if the XPS package contains a VisualBrush element with a Local Canvas.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>HasVisualBrushWithLocalGlyphs</p></td>
<td align="left"><p>bool</p></td>
<td align="left"><p>True if the XPS package contains a VisualBrush element with a Local Glyphs.</p></td>
</tr>
<tr class="even">
<td align="left"><p>HasVisualBrushWithLocalPath</p></td>
<td align="left"><p>bool</p></td>
<td align="left"><p>True if the XPS package contains a VisualBrush element with a Local Path.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>HasVisualBrushWithNonDefaultViewBox</p></td>
<td align="left"><p>bool</p></td>
<td align="left"><p>True if the XPS package contains a VisualBrush element with a NonDefault ViewBox (0, 0, 1, 1).</p></td>
</tr>
<tr class="even">
<td align="left"><p>HasVisualBrushWithNonDefaultViewPort</p></td>
<td align="left"><p>bool</p></td>
<td align="left"><p>True if the XPS package contains a VisualBrush element with a NonDefault ViewPort (0, 0, 1, 1).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>HasVisualBrushWithRemoteCanvas</p></td>
<td align="left"><p>bool</p></td>
<td align="left"><p>True if the XPS package contains a VisualBrush element with a Remote Canvas.</p></td>
</tr>
<tr class="even">
<td align="left"><p>HasVisualBrushWithRemoteGlyphs</p></td>
<td align="left"><p>bool</p></td>
<td align="left"><p>True if the XPS package contains a VisualBrush element with a Remote Glyphs.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>HasVisualBrushWithRemotePath</p></td>
<td align="left"><p>bool</p></td>
<td align="left"><p>True if the XPS package contains a VisualBrush element with a Remote Path.</p></td>
</tr>
<tr class="even">
<td align="left"><p>ImageBrushCount</p></td>
<td align="left"><p>long</p></td>
<td align="left"><p>The total number of ImageBrush elements in the XPS package.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>ImageBrushTileMode</p></td>
<td align="left"><p>string</p></td>
<td align="left"><p>The TileMode value of the ImageBrush element.</p></td>
</tr>
<tr class="even">
<td align="left"><p>ImageBrushType</p></td>
<td align="left"><p>string</p></td>
<td align="left"><p>The Image type value of the ImageBrush element.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>LinearGradientBrushColorInterpolationMode</p></td>
<td align="left"><p>string</p></td>
<td align="left"><p>The ColorInterpolationMode value of the LinearGradientBrush element.</p></td>
</tr>
<tr class="even">
<td align="left"><p>LinearGradientBrushColorType</p></td>
<td align="left"><p>string</p></td>
<td align="left"><p>The Color Type value of the LinearGradientBrush element.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>LinearGradientBrushContextColorChannelCount</p></td>
<td align="left"><p>string</p></td>
<td align="left"><p>The Context Color Channel Count value of the LinearGradientBrush element.</p></td>
</tr>
<tr class="even">
<td align="left"><p>LinearGradientBrushCount</p></td>
<td align="left"><p>long</p></td>
<td align="left"><p>The total number of LinearGradientBrush elements in the XPS package.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>LinearGradientBrushSpreadMethod</p></td>
<td align="left"><p>string</p></td>
<td align="left"><p>The SpreadMethod value of the LinearGradientBrush element.</p></td>
</tr>
<tr class="even">
<td align="left"><p>LinkTargetsCount</p></td>
<td align="left"><p>long</p></td>
<td align="left"><p>The total number of LinkTargets elements in the XPS package.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>LocalDictionaryContent</p></td>
<td align="left"><p>string</p></td>
<td align="left"><p>The type of Sharable Object found in this Local Dictionary.</p></td>
</tr>
<tr class="even">
<td align="left"><p>MaxGlyphsFontRenderingEMSize</p></td>
<td align="left"><p>long</p></td>
<td align="left"><p>The maximum FontRenderingEmSize in a Glyphs element.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>MaxGlyphsIndicesInAGlyphs</p></td>
<td align="left"><p>long</p></td>
<td align="left"><p>The maximum size of Indices in a Glyphs element.</p></td>
</tr>
<tr class="even">
<td align="left"><p>MaxGlyphsMappingsInAGlyphs</p></td>
<td align="left"><p>long</p></td>
<td align="left"><p>The maximum size of Mappings in a Glyphs element.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>MaxGlyphsProhibitedCaretStopCountInAGlyphs</p></td>
<td align="left"><p>long</p></td>
<td align="left"><p>The maximum size of ProhibitedCaretStopCount in a Glyphs element.</p></td>
</tr>
<tr class="even">
<td align="left"><p>MaxGradientStopsInALinearGradientBrush</p></td>
<td align="left"><p>long</p></td>
<td align="left"><p>The maximum number of GradientStops in a LinearGradientBrush element.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>MaxGradientStopsInARadialGradientBrush</p></td>
<td align="left"><p>long</p></td>
<td align="left"><p>The maximum number of GradientStops in a RadialGradientBrush element.</p></td>
</tr>
<tr class="even">
<td align="left"><p>MaxStrokeDashesInAPath</p></td>
<td align="left"><p>long</p></td>
<td align="left"><p>The maximum number of StrokeDashes in a Path element.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>PageDimension</p></td>
<td align="left"><p>string</p></td>
<td align="left"><p>The width and height of a Page in the XPS package.</p></td>
</tr>
<tr class="even">
<td align="left"><p>PageLanguage</p></td>
<td align="left"><p>string</p></td>
<td align="left"><p>The language of the page.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>PageThumbnailType</p></td>
<td align="left"><p>string</p></td>
<td align="left"><p>The Image type of the Page-level thumbnail.</p></td>
</tr>
<tr class="even">
<td align="left"><p>PathCount</p></td>
<td align="left"><p>long</p></td>
<td align="left"><p>The total number of Path elements in the XPS package.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>PathFillBrush</p></td>
<td align="left"><p>string</p></td>
<td align="left"><p>The brush type of the Path Fill.</p></td>
</tr>
<tr class="even">
<td align="left"><p>PathLanguage</p></td>
<td align="left"><p>string</p></td>
<td align="left"><p>The Language value of the Path element.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>PathOpacityMaskBrush</p></td>
<td align="left"><p>string</p></td>
<td align="left"><p>Type of Brush of the Path OpacityMask.</p></td>
</tr>
<tr class="even">
<td align="left"><p>PathStrokeBrush</p></td>
<td align="left"><p>string</p></td>
<td align="left"><p>The brush type of the Path Stroke property.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>PathStrokeDashCap</p></td>
<td align="left"><p>string</p></td>
<td align="left"><p>The StrokeDashCap type of the Path element.</p></td>
</tr>
<tr class="even">
<td align="left"><p>PathStrokeEndLineCap</p></td>
<td align="left"><p>string</p></td>
<td align="left"><p>The StrokeEndLineCap value of the Path element.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>PathStrokeLineJoin</p></td>
<td align="left"><p>string</p></td>
<td align="left"><p>The StrokeLineJoin value of the Path element.</p></td>
</tr>
<tr class="even">
<td align="left"><p>PathStrokeStartLineCap</p></td>
<td align="left"><p>string</p></td>
<td align="left"><p>The StrokeStartLineCap value of the Path element.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>RadialGradientBrushColorInterpolationMode</p></td>
<td align="left"><p>string</p></td>
<td align="left"><p>The ColorInterpolationMode value of the RadialGradientBrush element.</p></td>
</tr>
<tr class="even">
<td align="left"><p>RadialGradientBrushColorType</p></td>
<td align="left"><p>string</p></td>
<td align="left"><p>The Color Type value of the RadialGradientBrush element.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>RadialGradientBrushContextColorChannelCount</p></td>
<td align="left"><p>string</p></td>
<td align="left"><p>The Context Color Channel Count of the RadialGradientBrush element.</p></td>
</tr>
<tr class="even">
<td align="left"><p>RadialGradientBrushCount</p></td>
<td align="left"><p>long</p></td>
<td align="left"><p>The total number of RadialGradientBrush elements in the XPS package.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>RadialGradientBrushEllipseOrCircle</p></td>
<td align="left"><p>string</p></td>
<td align="left"><p>Defines whether the gradient brush is an ellipse or circle.</p></td>
</tr>
<tr class="even">
<td align="left"><p>RadialGradientBrushSpreadMethod</p></td>
<td align="left"><p>string</p></td>
<td align="left"><p>The SpreadMethod value of the RadialGradientBrush element.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>RemoteDictionaryContent</p></td>
<td align="left"><p>string</p></td>
<td align="left"><p>The type of Sharable Object found in this Remote Dictionary.</p></td>
</tr>
<tr class="even">
<td align="left"><p>SolidColorBrushColorType</p></td>
<td align="left"><p>string</p></td>
<td align="left"><p>The Color Type of the SolidColorBrush element.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>SolidColorBrushContextColorChannelCount</p></td>
<td align="left"><p>string</p></td>
<td align="left"><p>The Context Color Channel Count of the SolidColorBrush element.</p></td>
</tr>
<tr class="even">
<td align="left"><p>SolidColorBrushCount</p></td>
<td align="left"><p>long</p></td>
<td align="left"><p>The total number of SolidColorBrush elements in the XPS package.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>VisualBrushCount</p></td>
<td align="left"><p>long</p></td>
<td align="left"><p>The total number of VisualBrush elements in the XPS package.</p></td>
</tr>
<tr class="even">
<td align="left"><p>VisualBrushTileMode</p></td>
<td align="left"><p>string</p></td>
<td align="left"><p>The TileMode value of the VisualBrush element.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>VisualCount</p></td>
<td align="left"><p>long</p></td>
<td align="left"><p>The total number of Visuals in the XPS package.</p></td>
</tr>
</tbody>
</table>

## Digital Signature Rules

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Rule name</th>
<th align="left">Data type</th>
<th align="left">Explanation</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>CorruptedDigitalSignature</p></td>
<td align="left"><p>bool</p></td>
<td align="left"><p>True if the XPS package contains a corrupted digital signature.</p></td>
</tr>
<tr class="even">
<td align="left"><p>SignatureCount</p></td>
<td align="left"><p>long</p></td>
<td align="left"><p>The total number of digital signatures in the XPS package.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>XpsSignaturePolicy</p></td>
<td align="left"><p>string</p></td>
<td align="left"><p>The XPS Signature Policy value of the Signature element.</p></td>
</tr>
<tr class="even">
<td align="left"><p>HasInvalidXpsSignature</p></td>
<td align="left"><p>bool</p></td>
<td align="left"><p>True if the XPS package contains an invalid XPS Signature element.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>XpsSignatureStatus</p></td>
<td align="left"><p>string</p></td>
<td align="left"><p>The Signature Status value of the Signature element in the case where the signature is invalid. In other words, this rule is only enabled when HasInvalidXpsSignature is True.</p></td>
</tr>
<tr class="even">
<td align="left"><p>MaxNumberOfCertificatesInASignature</p></td>
<td align="left"><p>long</p></td>
<td align="left"><p>The maximum number of certificates found in a Signature element.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>HasXpsSignatureWithEmptyID</p></td>
<td align="left"><p>bool</p></td>
<td align="left"><p>True if the XPS package contains an XPS Signature element with empty ID.</p></td>
</tr>
<tr class="even">
<td align="left"><p>SignatureTimeFormat</p></td>
<td align="left"><p>string</p></td>
<td align="left"><p>The Signature Time Format value of the Signature element.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>MaxNumberOfCustomObjectsInASignature</p></td>
<td align="left"><p>long</p></td>
<td align="left"><p>The maximum number of Custom Objects found in a Signature element.</p></td>
</tr>
<tr class="even">
<td align="left"><p>MaxNumberOfCustomReferencesInASignature</p></td>
<td align="left"><p>long</p></td>
<td align="left"><p>The maximum number of Custom References found in a Signature element.</p></td>
</tr>
</tbody>
</table>

## Miscellaneous Rules

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Rule name</th>
<th align="left">Data type</th>
<th align="left">Explanation</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>CorruptedPageRendering</p></td>
<td align="left"><p>bool</p></td>
<td align="left"><p>True if the XPS package contains a non-renderable page.</p></td>
</tr>
</tbody>
</table>
