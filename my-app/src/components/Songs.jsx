import React from 'react';
import axios from 'axios';
import { Fragment } from 'react';
import {useState,useEffect} from 'react';
import SimilarSongs from './SimilarSongs'

function Songs(props) {
  // state for recommended songs
  const [songs, setSongs] = useState({});
  // state for similar songs
  const [similarSongs,setSimilarSongs]=useState({});
  const [lastHeardSong,setLastHeardSong]=useState("");
  
  //setting initial state
  useEffect(()=>{
    fetch("/api/songs")
    .then((res) => res.json())
    .then(
      (result) => {
          console.log('setting initial state of recommended songs')
          setSongs(result)
          // console.log(result);
      },
      (error) => {
        console.log(error);
      }
    )
  },[]);

  //retrieves list of similar songs to recommended songs when clicked
  //sets the similarSongs state to retrieved songs
  function similarSongsHandler(track,artist)
  {
    let currentSong=track+" "+artist;
    if(lastHeardSong===currentSong)
    {
      return;
    }
    setLastHeardSong(currentSong);
    axios.post('/api/songs/similar', {
      track:track,
      artist:artist
    })
    .then(function (response) {
      setSimilarSongs(response['data'])
    })
    .catch(function (error) {
      console.log(error);
    });
  }
  
  //whenever props changes this side effect is triggered
  useEffect(() => {
    console.log('in useEffect recommended songs')
    // console.log(props['songs'])
    setSongs(props['songs'])
  },[props['songs']]);
  
  

  //styles for Songs component
  let divStyle = {
  padding:"10px",
  textAlign:'center',
  width:"fit-content",
  position:'absolute',
  left:'150px',
  top:'50px',
  display:'inline-block'
}

  return (
    <div>
        <div className="border border-dark" style={divStyle}>
          <h1>Listen</h1>
          <Fragment >
            {
                Object.keys(songs).map((name, i) => (
                <p key={i} className="border-bottom">
                    <a href={songs[name][0]} onClick={() => similarSongsHandler(name,songs[name][1])} target="_blank" rel="noreferrer">{name}</a>
                </p>
                ))
            }
          </Fragment>
        </div>
        <SimilarSongs songs={similarSongs}/>
    </div>
    
  );
}

export default Songs