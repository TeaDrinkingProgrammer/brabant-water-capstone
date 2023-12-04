# Manual pre-data-cleaning
RUC0001_WTH_RIO_DWA.Bergingspercentage and RUC0030_WTH_RIO.Bergingspercentage use comma notation instead of semicolons and uses commas in the text
1. Remove the three unnessecary commas at the end of each line in the metadata header.
2. Replace all commas by `;`
3. Replace everything that matches the following regex with commas (the regex match any `;` after a bracket): `(?<=\));`

You can use the search and replace function in VS-code to this. You do need to turn regex matching on in the searchfield
