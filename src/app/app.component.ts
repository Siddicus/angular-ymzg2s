import { Component } from '@angular/core';

@Component({
  selector: 'my-app',
  templateUrl: './app.component.html',
  styleUrls: [ './app.component.css' ]
})

export class AppComponent  {
  name = '';
  matrix = [
    [
      1,0,1,0,0
    ],
    [
      0,0,0,0,1
    ],
    [
      1,0,1,1,0
    ],
    [
      0,0,0,0,0
    ],
    [
      0,1,0,1,0
    ]
  ];
}
