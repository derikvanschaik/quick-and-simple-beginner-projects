window.onload = (event) => {
    const canvas = document.getElementById("canvas");
    const ctx = canvas.getContext('2d');
    const rectBanner = document.getElementById("rect-update"); 
    // these are the offsets when we introduce html elements onto dom 
    // Easiest way to get these is by clicking the rectangle and console logging the 
    // event.x and event.y locations. 
    const winHorizOffset = 6; 
    const winVertOffset = 94;
    // function for drawing square on canvas
    const draw_square = (x, y, width, height) =>{
        ctx.fillStyle = 'orange'; 
        ctx.fillRect(x , y, width, height);
    }
    const in_bounds = (x, y, square_x, square_y, square_w, square_h) =>{
        const inBounds = x>= square_x && x <= square_x + square_w && y >= square_y && y <= square_y + square_h; 
        return inBounds; 
    }

    let lastLocation = [];
    let moving = false; 
    const square = {x :10,y:10, width: 20, height: 20};
    // draw square for square object 
    draw_square(
        square.x, square.y, square.width, square.height
    ); 


    canvas.onclick = (event) =>{

        const clickedOnSquare = in_bounds(
                event.x - winHorizOffset, event.y - winVertOffset,
                square.x, square.y,
                square.width, square.height
            );

        if (clickedOnSquare && !moving){
            moving = true;
            console.log("moving"); 
            // push the last locations of the square
            if (!lastLocation.length){
                lastLocation.push(square.x);
                lastLocation.push(square.y);
            } 
        }else{
                moving = false; 
        }
        // update rect-update banner
        rectBanner.textContent = 
        `Location: (${square.x}, ${square.y}), Moving: ${moving}`;
    }
    canvas.onmousemove = (event) =>{
        if (!moving){
            return; 
        }
        const width = 20;
        const height = 20;
        /* console.log(lastLocation); */ 
        if (lastLocation.length > 0){
            [x, y] = lastLocation; 
            ctx.clearRect(x, y, width, height);
            lastLocation.pop(); 
            lastLocation.pop();
            console.log(lastLocation); 
        }
        draw_square(event.x - winHorizOffset -20 , event.y - winVertOffset - 20 ,width, height);
        lastLocation.push(event.x - winHorizOffset -20);
        lastLocation.push(event.y - winVertOffset - 20);
        // update the values of square object 
        square.x = event.x - winHorizOffset-20; 
        square.y = event.y - winVertOffset -20; 
        square.width = width;
        square.height = height;
        // update rect-update banner
        rectBanner.textContent = 
        `Location: (${square.x}, ${square.y}), Moving: ${moving}`;
    } 

}

