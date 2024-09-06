#!/usr/bin/node
import { promisify } from 'util';
const request = promisify(require('request'));
const planetsID = process.argv[2];

async function starwarsCharacters (planetsID) {
  const endpoint = 'https://swapi-api.alx-tools.com/api/planets/3/' + planetsID;
  let response = await (await request(endpoint)).body;
  response = JSON.parse(response);
  const characters = response.characters;

  for (let i = 0; i < characters.length; i++) {
    const urlCharacter = characters[i];
    let character = await (await request(urlCharacter)).body;
    character = JSON.parse(character);
    console.log(character.name);
  }
}

starwarsCharacters(planetsID);