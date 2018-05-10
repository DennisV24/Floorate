# Copyright © 2018 This material is the property of the individuals that contributed to it: Dennis Vidovic, Andrew Rae, Thomas Kidd and Yusef Zia.
# It may NOT be copied or otherwise used, in part or in its entirety, without permission, for any purpose, other than to execute it on a computing
# platform as a complete project, without modifications.

from spritesList import *

movementDicts = {
    'LightInfantry': {
        TerrainTypes.waterTile: None,
        TerrainTypes.grassTile: 1.,
        TerrainTypes.plainTile: 1.,
        TerrainTypes.mountainTile: 2.,
        TerrainTypes.forestTile: 1.,
        TerrainTypes.cityTile: 1.,
    },
    'Battleship': {
        TerrainTypes.waterTile: 1.,
        TerrainTypes.grassTile: None,
        TerrainTypes.plainTile: None,
        TerrainTypes.mountainTile: None,
        TerrainTypes.forestTile: None,
        TerrainTypes.cityTile: None,
    }
}