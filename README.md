# pyGAMESS-DS
# Este script tem como finalidade automatizar a retirada das principais informações do GAMESS-US. São elas: 

- Coordenadas achadas pela otimização da geometria (caso exista).
- Energia total livre no solvente
- Interação total (DELTA + ES + CAV + DISP + REP)
- Valores das correções das energia de Gibbs
- Primeira frequência vibracional
- "Net Charges"

# Instalação (WINDOWS):

- Coloque o executável em uma pasta com todos os arquivos gerados pelo GAMESS-US (Obs: eles devem estar sempre aos pares, e nomeados da seguinte maneira: E1.out, G1.out, E2.out, G2.out, E3.out, G3.out,...).
- basta executar como administrador.
- Ao final será gerado um LOG em C:/LOG_pyGAMESS-DataScan
