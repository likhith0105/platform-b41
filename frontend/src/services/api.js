const API_BASE = 'http://localhost:5000/api';
const API_KEY = import.meta.env.VITE_BACKEND_API_KEY || '';
const API_HEADERS = API_KEY ? { 'X-API-KEY': API_KEY } : {};

export const fetchStations = async () => {
  const resp = await fetch(`${API_BASE}/trains/stations`, { headers: API_HEADERS });
  if (!resp.ok) throw new Error('Failed to fetch stations');
  return resp.json();
};

export const fetchPosition = async (trainNumber, coach, station) => {
  const url = `${API_BASE}/platformposition?train_number=${trainNumber}&coach=${coach}&station=${station}`;
  const resp = await fetch(url, { headers: API_HEADERS });
  if (!resp.ok) throw new Error('Could not find position for this combination');
  return resp.json();
};

export const fetchGuide = async (trainNumber, coach, station) => {
  const resp = await fetch(`${API_BASE}/platformguide/${trainNumber}/${coach}/${station}`, { headers: API_HEADERS });
  if (!resp.ok) throw new Error('Failed to fetch guide');
  return resp.json();
};
