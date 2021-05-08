// class App extends Component{
//     // state of the class object
//     state={
//         tags:['hello','I','Am','Pushpendra']
//     }
//     styles={
//         fontSize:10
//     };
//     // constructor(){
//     //     super();
//     //     //to make handleSongs access this using bind function
//     //     this.handleSongs=this.handleSongs.bind(this);
//     //or make the handleSongs function as arrow function
//     // }
//     render(){
//         // javascript expressions could be rendered using {}
//         //call methods for rendering as {this.fx()}
//         //conditional statements in render {this.count==0&&'hi there'}
//         return (
//             // access data passed to components using this.props
//             <div>
//                 <p style={this.styles}>cake chat server</p>
//                 {/* passing parameters to onClick method */}
//                 <button className="btn btn-primary" onClick={()=>this.handleSongs('hi')}>songs</button>
//                 <Tone tone={'neutral'}/>
//                 {/* key must be distinct for each element of array */}
//                 <ul>{this.state.tags.map(tag=><li key={tag}>{tag}</li>)}</ul>
//             </div>
//         );
//     }
//     // define helper functions
//     handleSongs =(str)=>{
//         console.log('clicked');
//         console.log(this);
//         console.log(str)
//         //change state using setState() method
//         //only the elements which are affected are changed in ui nothing else is affected
//         this.setState({tags:[]})
//     }
//     fx(){
        
//     }
// }
