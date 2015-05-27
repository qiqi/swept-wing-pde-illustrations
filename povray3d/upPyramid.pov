#include "colors.inc"
#include "shapes.inc"

camera {
  location < 2,  2, -5> 
  look_at  <-1, -1, -1>
}
#local s = (1 - $t);
union {
  box {
    <-s,-s,-s>,  // Near lower left corner
    <+s,+s,+s>   // Far upper right corner
    pigment { Green filter .8 }
  }
  box {
    <-2-s,-s,-s>,  // Near lower left corner
    <-2+s,+s,+s>   // Far upper right corner
    pigment { Red filter .8 }
  }
  box {
    <-s,-2-s,-s>,  // Near lower left corner
    <+s,-2+s,+s>   // Far upper right corner
    pigment { Blue filter .8 }  
  }       
  box {   
    <-2-s,-2-s,-s>,  // Near lower left corner
    <-2+s,-2+s,+s>   // Far upper right corner
    pigment { Magenta filter .8 }
  }       
  box {   
    <-s,-s,-2-s>,  // Near lower left corner
    <+s,+s,-2+s>   // Far upper right corner
    pigment { Yellow filter .8 }
  }       
  box {   
    <-2-s,-s,-2-s>,  // Near lower left corner
    <-2+s,+s,-2+s>   // Far upper right corner
    pigment { Blue filter .8 }  
  }       
  box {   
    <-s,-2-s,-2-s>,  // Near lower left corner
    <+s,-2+s,-2+s>   // Far upper right corner
    pigment { Red filter .8 }   
  }       
  box {   
    <-2-s,-2-s,-2-s>,  // Near lower left corner
    <-2+s,-2+s,-2+s>   // Far upper right corner
    pigment { Green filter .8 }                     
  }       
}               
light_source { <2, 4, -3> color White}

