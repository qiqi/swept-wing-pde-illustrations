#include "colors.inc"
#include "shapes.inc"

camera {
  location < 2,  2, -5> 
  look_at  <-1, -1, -1>
}
#local s = (1 - $t);
union {
  #for (i,-2,0,2)
  #for (j,-2,0,2)
  #for (k,-2,0,2)
  box {
    <i-s,j-s,k-s>,  // Near lower left corner
    <i+s,j+s,k+s>   // Far upper right corner
    pigment { Gray filter .98 }
  }
  #end
  #end
  #end

  #for (j,-2,0,2)
  #for (k,-2,0,2)
  box {
    <-2+s,j-s,k-s>,  // Near lower left corner
    <  -s,j+s,k+s>   // Far upper right corner
    pigment { Gray filter .98 }
  }
  box {
    <-3  ,j-s,k-s>,  // Near lower left corner
    <-2-s,j+s,k+s>   // Far upper right corner
    pigment { Gray filter .98 }
  }
  box {
    <+s,j-s,k-s>,  // Near lower left corner
    < 1,j+s,k+s>   // Far upper right corner
    pigment { Gray filter .98 }
  }
  #end
  #end

  #for (i,-2,0,2)
  #for (k,-2,0,2)
  box {
    <i-s,-2+s,k-s>,  // Near lower left corner
    <i+s,  -s,k+s>   // Far upper right corner
    pigment { Gray filter .98 }
  }
  box {
    <i-s,-3  ,k-s>,  // Near lower left corner
    <i+s,-2+s,k+s>   // Far upper right corner
    pigment { Gray filter .98 }
  }
  box {
    <i-s,s,k-s>,  // Near lower left corner
    <i+s,1,k+s>   // Far upper right corner
    pigment { Gray filter .98 }
  }
  #end
  #end

  #for (i,-2,0,2)
  #for (j,-2,0,2)
  box {
    <i-s,j-s,-2+s>,  // Near lower left corner
    <i+s,j+s,  -s>   // Far upper right corner
    pigment { Gray filter .98 }
  }
  box {
    <i-s,j-s,-3  >,  // Near lower left corner
    <i+s,j+s,-2+s>   // Far upper right corner
    pigment { Gray filter .98 }
  }
  box {
    <i-s,j-s,s>,  // Near lower left corner
    <i+s,j+s,1>   // Far upper right corner
    pigment { Gray filter .98 }
  }
  #end
  #end

  #for (i,-2,0,2)
  #for (j,-3,1,2)
  #for (k,-3,1,2)
  box {
    <i-s,max(-3,j-1+s),max(-3,k-1+s)>,  // Near lower left corner
    <i+s,min( 1,j+1-s),min( 1,k+1-s)>   // Far upper right corner
    pigment { Red filter .8 }
  }
  #end
  #end
  #end

  #for (i,-3,1,2)
  #for (j,-2,0,2)
  #for (k,-3,1,2)
  box {
    <max(-3,i-1+s),j-s,max(-3,k-1+s)>,  // Near lower left corner
    <min( 1,i+1-s),j+s,min( 1,k+1-s)>   // Far upper right corner
    pigment { Green filter .8 }
  }
  #end
  #end
  #end

  #for (i,-3,1,2)
  #for (j,-3,1,2)
  #for (k,-2,0,2)
  box {
    <max(-3,i-1+s),max(-3,j-1+s),k-s>,  // Near lower left corner
    <min( 1,i+1-s),min( 1,j+1-s),k+s>   // Far upper right corner
    pigment { Blue filter .8 }
  }
  #end
  #end
  #end
}               
light_source { <2, 4, -3> color White}

