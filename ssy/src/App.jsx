import 'bootstrap/dist/css/bootstrap.css';
import { useState } from 'react';
function zapisz_na_kurs(){
 const kursy = ["Programowanie w C#","Angular dla początkujących", "Kurs Django"];
const [imie, setImie]=useState("");
const [kurs, setKurs]=useState("");

const handlesubmit = (e)=>{e.preventDefault();

console.log(imie);
const indeks = parseInt(kurs) - 1;

if(indeks >= 0 && indeks<kursy.length){
  console.log(kursy[indeks]);
}else{
  console.log("Nieprawindeksłowy numer kursu");
}
};
    return(
      <>
      <h1>Liczba kursów: {kursy.length} </h1>
      <ol>
        {kursy.map((nazwakurs, index)=>
        (<li key={index}>{nazwakurs}</li>))}
        </ol>
        <form onSubmit={handlesubmit}>
        <label htmlFor="imie_nazwisko">Imię i nazwisko:</label><br />
        <input type="text" id="imie_nazwisko" value={imie} onChange={(e) =>setImie(e.target.value)} /><br />
        <label htmlFor="nr-kursu">Numer kursu:</label><br />
        <input
            type="number"
            value={kurs}
            onChange={(e) => setKurs(e.target.value)}
            className="form-control"
            id="numerKursu"
            required
          /><br />
        <button type="submit" className="btn btn-primary">Zapisz do kursu</button><br />
        </form>
        </>
    );
}
export default zapisz_na_kurs;